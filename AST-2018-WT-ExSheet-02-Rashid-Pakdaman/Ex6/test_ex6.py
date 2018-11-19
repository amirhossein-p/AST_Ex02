import unittest
import ex6
import numpy as np

class testCase(unittest.TestCase):

	def test_calcSum(self):
		self.assertEqual(ex6.calcSum([1,2,3,4,5]), 1+2+3+4+5)

	def test_calcProduct(self):
		self.assertEqual(ex6.calcProduct([1,2,3,4,5]), 1*2*3*4*5)

	def test_calcAverage(self):
		self.assertEqual(ex6.calcAverage([1,2,3,4,5]), (1+2+3+4+5)/5)

	def test_calcVariance(self):
		self.assertEqual(ex6.calcVariance([1,2,3,4,5]), np.var([1,2,3,4,5]))

	def test_calcMin(self):
		self.assertEqual(ex6.calcMin([1,2,3,4,5]), 1)

	def test_calcMax(self):
		self.assertEqual(ex6.calcMax([1,2,3,4,5]), 5)

if __name__ == '__main__':
	unittest.main()
