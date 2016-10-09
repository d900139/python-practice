###################
##  unittest2
###################


import unittest

from assign2 import biggest3

class test_cmp(unittest.TestCase):
    def test1(self):
        self.assertEqual(biggest3('2134,3412,6421,8723,9239,1234,2345'), [9239, 8723, 6421])
    def test2(self):
        self.assertEqual(biggest3('333,999,222,777,444,666,000,555,888,111'),[999,888,777])

if __name__ == '__main__':
    unittest.main()



