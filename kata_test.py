import unittest
from kata import calAdd

class testCalAdd(unittest.TestCase):
    """
    Basic cal test class
    """

    def test_twoNumbers(self):
        res = calAdd('1','2')
        self.assertEqual(res, 3)

		
if __name__ == '__main__':
    unittest.main()
