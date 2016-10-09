import unittest
import re
from assign3 import convert_sum

class test_add(unittest.TestCase):
    def test1(self):
	self.assertEqual(convert_sum('"CDEF","ABC","FIJK"'),150)
    def test2(self):
 	self.assertEqual(convert_sum('"AAA","BBB"'),15)
    def test3(self):
	self.assertEqual(convert_sum('"AAA","BBB",""'),15)


if __name__ == '__main__':
	unittest.main()
