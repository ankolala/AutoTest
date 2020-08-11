#coding=utf-8

import unittest

def raise_error(*args, **kwds):
        raise ValueError('invalid value: %s%s' % (args, kwds))

class classname(unittest.TestCase):
    def setUp(self):
        print('start...')
        self.fixture = range(1, 10)
    
    def tearDown(self):
        print('end...')
        del self.fixture

    def test_1(self):
        self.assertTrue(self.fixture, range(1,10))

    def test_exception(self):
        try:
            raise_error('a', b='c')
        except ValueError:
            pass
        # self.fail('no ValueError')

        self.assertRaises(ValueError, raise_error, 'a', b='c')

if __name__ == "__main__":
    unittest.main()