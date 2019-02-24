from pizzaStructure import Pizza
from sliceStructure import Slice
import numpy as np
# list of slices


class PizzaManager:
	def __init__(self, pizza):
		self.pizza = pizza
		self.startSlices = self.allPossibleStartSlices()

	def allPossibleStartSlices(self):
		startSlices = []
		minSizeOfSlice = self.pizza.L * 4
		col = minSizeOfSlice
		row = 1
		combinations = []
		while col % 2 == 0:
			combinations.append((row, col))
			col = col//2
			row = minSizeOfSlice//col

		for combo in combinations:
			startSlices.append(Slice(0, 0, combo[0], combo[1]))

		for combo in combinations:
			startSlices.append(Slice(0, 0, combo[1], combo[0]))
			
		return startSlices


	def makeSlice(self):
		"""
		creates a slice object based on the pizza
		"""
		pass



if __name__ == "__main__":
	pizza = Pizza("inputFiles/a_example.in")
	pizzaManager = PizzaManager(pizza)
	for slice in pizzaManager.startSlices:
		print("Here's the slice you cut out: \n", pizza.cut(slice), end="\n")
		print("Now the pizza dish looks like this: \n", pizza.dish, end="\n\n")
		pizza.reset()