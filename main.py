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
sys.path.append('./controller')
sys.path.append('./report')
import core, runner, log, test_1, style_1, style_2
import logging
import datetime
# import configparser

if __name__ == "__main__":
    '''
    # 1、配置初始化
    conf = configparser.ConfigParser()
    conf.read('./config/config.ini', encoding='utf-8')

    # 获得配置文件中的所有sections
    print conf.sections()
    run_case = conf.get('Basic', 'run_case')
    create_report_by_style_1 = conf.get('Basic', 'create_report_by_style_1')
    create_report_by_style_2 = conf.get('Basic', 'create_report_by_style_2')
    print conf.options('Basic')

    
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(test_1.SimpleTestCase('test_exception'))
    suite.addTest(test_1.SimpleTestCase('test_1'))
    # 组装多个测试用例
    runner = unittest.TextTestRunner()
    runner.run(suite)
    '''
    log.set_level(logging.DEBUG)

    runner = runner.TestRunner()
    # 添加测试用例文件夹
    runner.add_case_dir(r"test")
    runner.run_test(report_title='auto_test_report')