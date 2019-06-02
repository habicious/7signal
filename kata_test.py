import unittest
from kata import calAdd

class testCalAdd(unittest.TestCase):
    """
    Basic cal test class
    """

    def test_twoStrings(self):
        res = calAdd('1','2')
        self.assertEqual(res, 3)

    def test_emptyString(self):
		res = calAdd('','2')
		self.assertEqual(res, 2)
		
    def test_oneString(self):
		res = calAdd('1')
		self.assertEqual(res, 1)
		
    def test_xStrings(self):
		res = calAdd('1','2','3','4','5')
		self.assertEqual(res, 15)
		
    def test_newLineStrings(self):
		res = calAdd('1,2,3')
		self.assertEqual(res, 6)
		
if __name__ == '__main__':
    unittest.main()
