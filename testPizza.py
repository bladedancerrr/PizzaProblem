import unittest
from pizzaStructure import Pizza

class TestPizza(unittest.TestCase):

	def testRows(self):
		pizza = Pizza("inputFiles/a_example.in")
		self.assertTrue(pizza.rows >= 1 and pizza.rows <= 1000)

	def testCols(self):
		pizza = Pizza("inputFiles/a_example.in")
		self.assertTrue(pizza.cols >= 1 and pizza.cols <= 1000)

	def testL(self):
		pizza = Pizza("inputFiles/a_example.in")
		self.assertTrue(pizza.L >= 1 and pizza.L <= 1000)

	def testH(self):
		pizza = Pizza("inputFiles/a_example.in")
		self.assertTrue(pizza.H >= 1 and pizza.H <= 1000)


	def testPizzaArray(self):
		pizza = Pizza("inputFiles/a_example.in")
		self.assertEqual(pizza.pizzaArray.shape, (pizza.rows, pizza.cols))
		

if __name__ == "__main__":
	unittest.main()