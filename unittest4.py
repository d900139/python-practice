###############
##  unittest4
###############

import unittest

from assign4_2 import summ

class testsumm(unittest.TestCase):
   def test1(self):
	self.assertEqual(summ(1,10),-55)
   def test2(self):
	self.assertEqual(summ(1,100),-5050)

if __name__ == '__main__':
   unittest.main()



