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
		
if __name__ == '__main__':
    unittest.main()
