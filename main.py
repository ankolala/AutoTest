#! /usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Created on 2020-08-11
@author: Rachel
@description: 编写unittest 测试用例
'''

import os, sys, unittest
sys.path.append('./test')
sys.path.append('./common')
sys.path.append('./report')
import core
import log
import test_1
import logging
import datetime
import configparser
import style_1, style_2

class _TestRunner:
    def __init__(self, report_dir, report_title, style1, style2, verbosity=1, description=""):
        self.report_dir = report_dir
        self.verbosity = verbosity
        self.title = report_title
        self.style1 = style1
        self.style2 = style2
        self.description = description
        self.start_time = datetime.datetime.now()
        self.stop_time = None

    def run(self, test):
        msg = "开始测试，用例数量总共{}个，跳过{}个，实际运行{}个"
        log.info(msg.format(Tool.total_case_num,
                            Tool.total_case_num - Tool.actual_case_num,
                            Tool.actual_case_num))
        result = _TestResult(self.verbosity)
        test(result)
        self.stop_time = datetime.datetime.now()
        self.analyze_test_result(result)
        log.info('Time Elapsed: {}'.format(self.stop_time - self.start_time))

        if style1:
            file_path = os.path.join(self.report_dir,
                                     r"{}-style-1.html".format(self.start_time.strftime("%Y-%m-%d-%H-%M-%S")))
            style_1.build_report(file_path, result_data)

        if style2:
            file_path = os.path.join(self.report_dir,
                                     r"{}-style-2.html".format(self.start_time.strftime("%Y-%m-%d-%H-%M-%S")))
            style_2.build_report(file_path, result_data)

    @staticmethod
    def sort_result(case_results):
        rmap = {}
        classes = []
        for n, t, o, e, run_time in case_results:
            cls = t.__class__
            if cls not in rmap:
                rmap[cls] = []
                classes.append(cls)
            rmap[cls].append((n, t, o, e, run_time))
        r = [(cls, rmap[cls]) for cls in classes]
        return r

    def analyze_test_result(self, result):
        result_data["reportName"] = self.title
        result_data["beginTime"] = str(self.start_time)[:19]
        result_data["totalTime"] = str(self.stop_time - self.start_time)

        sorted_result = self.sort_result(result.result)
        for cid, (cls, cls_results) in enumerate(sorted_result):
            pass_num = fail_num = error_num = skip_num = 0
            for case_state in cls_results:
            # for case_state, *_ in cls_results:
                if case_state == 0:
                    pass_num += 1
                elif case_state == 1:
                    fail_num += 1
                elif case_state == 2:
                    error_num += 1
                else:
                    skip_num += 1

            name = "{}.{}".format(cls.__module__, cls.__name__)
            global current_class_name
            current_class_name = name

            for tid, (state_id, t, o, e, run_time) in enumerate(cls_results):

                name = t.id().split('.')[-1]
                doc = t.shortDescription() or ""
                case_data = dict()
                case_data['className'] = current_class_name
                case_data['methodName'] = name
                case_data['spendTime'] = "{:.2}S".format(run_time)
                case_data['description'] = doc
                case_data['log'] = o + e
                if STATUS[state_id] == "Pass":
                    case_data['status'] = "成功"
                if STATUS[state_id] == "Fail":
                    case_data['status'] = "失败"
                if STATUS[state_id] == "Error":
                    case_data['status'] = "错误"
                if STATUS[state_id] == "Skip":
                    case_data['status'] = "跳过"
                result_data['testResult'].append(case_data)

        result_data["testPass"] = result.success_count
        result_data["testAll"] = result.success_count + result.failure_count + result.error_count + result.skip_count
        result_data["testFail"] = result.failure_count
        result_data["testSkip"] = result.skip_count
        result_data["testError"] = result.error_count

class TestRunner(object):
    def __init__(self):
        self.case_dirs = []

    def add_case_dir(self, dir_path):
        if not os.path.exists(dir_path):
            raise Exception("test_case_dir is not exist：{}".format(dir_path))
        elif dir_path in self.case_dirs:
            log.warn("test_case_dir existed：{}".format(dir_path))
        else:
            self.case_dirs.append(dir_path)

    def run_test(self, report_title='auto_test_report', style1=True, style2=True):

        if not self.case_dirs:
            raise Exception("please execute add_case_dir func first")

        if not os.path.exists("report"):
            os.mkdir("report")

        report_dir = os.path.abspath("report")
        suite = unittest.TestSuite()
        for case_path in self.case_dirs:
            suite.addTests(unittest.TestLoader().discover(case_path))
        _TestRunner(report_dir=report_dir, report_title=report_title, style1=style1, style2=style2).run(suite)

        os.system("start report")


if __name__ == "__main__":

    # 1、配置初始化
    conf = configparser.ConfigParser()
    conf.read('./config/config.ini', encoding='utf-8')

    # 获得配置文件中的所有sections
    print conf.sections()
    run_case = conf.get('Basic', 'run_case')
    create_report_by_style_1 = conf.get('Basic', 'create_report_by_style_1')
    create_report_by_style_2 = conf.get('Basic', 'create_report_by_style_2')
    print conf.options('Basic')

    '''
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(test_1.SimpleTestCase('test_exception'))
    suite.addTest(test_1.SimpleTestCase('test_1'))
    # 组装多个测试用例
    runner = unittest.TextTestRunner()
    runner.run(suite)
    '''
    log.set_level(logging.DEBUG)

    runner = TestRunner()
    runner.add_case_dir(r"test")
    runner.run_test(report_title='自动化测试报告', style1=create_report_by_style_1, style2=create_report_by_style_2)