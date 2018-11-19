import unittest
import ex5
import time

class testCase(unittest.TestCase):

    def test_calcPrime(self):
        self.assertEqual(ex5.calcPrime(100), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])


    def test_calcTime(self):
        self.assertLess(ex5.calcTime(ex5.calcPrime),0.5 )

if __name__ == '__main__':
    unittest.main()
