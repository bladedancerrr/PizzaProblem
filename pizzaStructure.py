import numpy as np
from sliceStructure import Slice
import matplotlib.pyplot as plt

class Dish:
	def __init__(self, pizza):
		self.dish = np.zeros(self.pizzaArray.shape, dtype=int)

class Pizza:
	rows = 0
	cols = 0
	L = 0
	H = 0

	pizzaArray = np.empty
	dish = np.empty

	def __init__(self, fileName):
		"""
		:type fileName: string

		This function takes a textFileName as input, finds that file in the same directory, processes it, 
		and updates the properties and pizzaDict
		"""
		file = open(fileName)
		lines = file.readlines()
		self.rows, self.cols, self.L, self.H = [int(val) for val in lines[0].split()]
		self.pizzaArray = np.array([list(map(lambda item: 1 if item == 'T' else 0, row.strip())) for row in lines[1:]])
		file.close()

		self.dish = np.zeros(self.pizzaArray.shape, dtype=int)

	def cut(self, slice):
		"""
		:type slice: Slice object
		"""
		self.dish[slice.startRow:slice.endRow + 1, slice.startCol:slice.endCol + 1] = 1
		return self.pizzaArray[slice.startRow:slice.endRow + 1, slice.startCol:slice.endCol + 1]

	def reset(self):
		self.dish = np.zeros(self.pizzaArray.shape, dtype=int)


if __name__ == "__main__":
	fileName = "inputFiles/a_example.in"
	print(f"\nUsing '{fileName}' as sample input file")
	pizza = Pizza(fileName)
	print("Number of rows of the Pizza: ", pizza.rows)
	print("The pizza looks like this: \n", pizza.pizzaArray, "\n\n")
	print("The dish looks like this: \n", pizza.dish, "\n")
	print("Please run testPizza.py to make sure this works properly.\n")

	print("Getting a slice...\n") 
	slice = Slice(0, 0, 2, 2)
	print("Let's cut out a piece!")
	print(pizza.cut(slice), "\n")
	print("The dish looks like this: \n", pizza.dish, "\n")

	print("Hey! Let's extend to the right!")
	slice.extendRight()
	print("Now, it looks like: ")
	print(pizza.cut(slice), "\n")
	print("The dish looks like this: \n", pizza.dish, "\n")
