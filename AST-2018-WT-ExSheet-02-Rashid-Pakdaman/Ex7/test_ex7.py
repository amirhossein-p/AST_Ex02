import unittest
import ex7

class testCase(unittest.TestCase):

    def test_funCalc(self):
        self.assertEqual(ex7.funCalc([0.5,0.8,2.0]),(8/7))

    def test_valueCalc(self):
        self.assertEqual(ex7.valueCalc(4,8),[0.5,0.9,0.9,0.1,0.1,0.1,0.1,0.1])

    def test_funCalc2Perc(self):
        self.assertEqual(ex7.funCalc2Perc([0.5,0.8,2.0]),1.14)

if __name__ == '__main__':
    unittest.main()
