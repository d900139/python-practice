import unittest

class perfectnum:
    def is_perfect(self,inputnum):
        li = [x for x in range(1,inputnum) if inputnum % x == 0]
        return sum(li) == inputnum
class testperfectnum(unittest.TestCase):
    def test1(self):
        per = perfectnum()
        self.assertEqual(per.is_perfect(6),True)
    def test2(self):
        per = perfectnum()
        self.assertEqual(per.is_perfect(8),False)
    def test3(self):
        per = perfectnum()                       
        self.assertEqual(per.is_perfect(28),True)

if __name__ == '__main__':
    unittest.main()
