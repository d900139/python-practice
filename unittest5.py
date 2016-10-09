#####################
##  unittest5
#####################

import unittest

from assign5 import fib

class test_fib(unittest.TestCase):
    def test1(self):
        c = fib()
        self.assertEqual(c.next(), 1)
        self.assertEqual(c.next(), 2)
        self.assertEqual(c.next(), 3)
        self.assertEqual(c.next(), 5)
        self.assertEqual(c.next(), 8)
    def test2(self):
        c = fib()
        self.assertEqual(c.next(), 1)
        self.assertEqual(c.next(), 2)
        self.assertEqual(c.next(), 3)
        self.assertEqual(c.next(), 5)
        self.assertEqual(c.next(), 8)

if __name__ == '__main__':
    unittest.main()
