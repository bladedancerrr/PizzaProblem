import unittest
import calc

class TestCalc(unittest.TestCase):

	def test_add(self):
		self.assertEqual(calc.add(10,5), 14)
		self.assertEqual(calc.add(-1, 1), 0)

	def test_subtract(self):
		self.assertEqual(calc.subtract(10,5), 5)
		self.assertEqual(calc.subtract(-1, 1), -2)



if __name__ == '__main__':
	unittest.main()