# coding=utf-8
#!/usr/bin/env python 
'''
Created on 2020-08-11
@author: Rachel
@description: 编写unittest 测试用例
'''

import sys, unittest
sys.path.append('./')
import test_1

if __name__ == "__main__":

    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(test_1.SimpleTestCase('test_exception'))
    suite.addTest(test_1.SimpleTestCase('test_1'))
    # 组装多个测试用例
    runner = unittest.TextTestRunner()
    runner.run(suite)