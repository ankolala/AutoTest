#!/usr/bin/env python

import unittest

def raise_error(*args, **kwds):
        raise ValueError('invalid value: %s%s' % (args, kwds))

class SimpleTestCase(unittest.TestCase):
    def setUp(self):
        print('start...')
        self.fixture = range(1, 10)
    
    def tearDown(self):
        print('end...')
        del self.fixture

    @unittest.skip('debug')
    def test_1(self):
        print 'exec test_1'
        self.assertTrue(self.fixture, range(1,10))

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