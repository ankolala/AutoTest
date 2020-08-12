#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
sys.path.append('./common')
import unittest
import log

def raise_error(*args, **kwds):
        raise ValueError('invalid value: %s%s' % (args, kwds))

class SimpleTestCase(unittest.TestCase):
    def setUp(self):
        log.info("start...")
        self.fixture = range(1, 10)
    
    def tearDown(self):
        log.info("end...")
        del self.fixture

    def test_1(self):
        log.info("exec test_1")
        self.assertTrue(self.fixture, range(1,10))

    @unittest.skip('debug')
    def test_exception(self):
        print 'exec test_execption'
        try:
            raise_error('a', b='c')
        except ValueError:
            pass
        # self.fail('no ValueError')

        self.assertRaises(ValueError, raise_error, 'a', b='c')

if __name__ == "__main__":
    unittest.main()