from pizzaStructure import Pizza
from sliceStructure import Slice, Cell
import numpy as np


def isValidSlice(self, slice):
		for row in range(slice.startRow, slice.endRow + 1):
			for col in range(slice.startCol, slice.endCol + 1):
				if row < 0 or row > pizza.rows - 1 or col < 0 or col > pizza.cols - 1 or pizza.dish[row, col] == 1:
					return False
		return True

def neighbourCells(pizza, slice):
		cells = []
		# on the left
		for row in range(slice.startRow, slice.endRow + 1):
			cell = Cell(row, slice.startCol - 1)
			if isValidSlice(pizza, cell):
				cells.append(cell)

		# on right
		for row in range(slice.startRow, slice.endRow + 1):
			cell = Cell(row, slice.endCol + 1)
			if isValidSlice(pizza, cell):
				cells.append(cell)

		# on top
		for col in range(slice.startCol, slice.endCol + 1):
			cell = Cell(slice.startRow - 1, col)
			if isValidSlice(pizza, cell):
				cells.append(cell)

		# on bottom
		for col in range(slice.startCol, slice.endCol + 1):
			cell = Cell(slice.endRow + 1, col)
			if isValidSlice(pizza, cell):
				cells.append(cell)

		return cells

def startSlices(pizza, startCell):
		startSlices = []
		minSizeOfSlice = pizza.L * 2
		col = minSizeOfSlice
		row = 1
		combinations = []
		while col % 2 == 0:
			combinations.append((row, col))
			col = col//2
			row = minSizeOfSlice//col

		for combo in combinations:
			slice = Slice(startCell.startRow, startCell.startCol, combo[0] - 1 + startCell.startRow, combo[1] - 1 + startCell.startCol)
			if isValidSlice(pizza, slice):
				slice.display(pizza)
				startSlices.append(slice)

		for combo in combinations:
			slice = Slice(startCell.startRow, startCell.startCol, combo[1] - 1 + startCell.startRow, combo[0] - 1 + startCell.startCol)
			if isValidSlice(pizza, slice):
				slice.display(pizza)				
				startSlices.append(slice)

		return startSlices

# list of slices
class PizzaManager:
	def __init__(self, pizza):
		self.pizza = pizza
		self.allValidSlicePaths = []

	def getAllPossibleValidSlicePaths(self):
		self.recursiveSlicePathFinder(self.pizza)

	def recursiveSlicePathFinder(self, pizza, cell=Cell(0, 0), slicePath=[]):
		# print("Start Cell: ", " ", (cell.startRow, cell.startCol))
		# print("Length of slicePath = ", len(slicePath), "\n")
		for slice in startSlices(pizza, cell):
			# print('created the slices\n')
			print("Slice: ", " ".join([str(slice.startRow), str(slice.startCol), str(slice.endRow), str(slice.endCol)]), "\n")
			localSlicePath = slicePath
			localPizza = pizza
			if isValidSlice(localPizza, slice):
				# print("Got a valid slice. Cutting...")
				# print(localPizza.cut(slice), "\n")
				localSlicePath.append(slice) 
				for cell in neighbourCells(localPizza, slice):
					# print("Cell: ", " ", (cell.startRow, cell.startCol), "\n")
					self.recursiveSlicePathFinder(localPizza, cell=cell, slicePath=localSlicePath)
			else:
				print("Appended: ", localSlicePath)
				print("***********\n")
				for slice in slicePath:
					print(" ".join([str(slice.startRow), str(slice.startCol), str(slice.endRow), str(slice.endCol)]))
					slice.display(localPizza)
				print("***********\n")

				self.allValidSlicePaths.append(localSlicePath)


if __name__ == "__main__":
	pizza = Pizza("inputFiles/a_example.in")
	pizzaManager = PizzaManager(pizza)
	pizzaManager.getAllPossibleValidSlicePaths()
	print("len ",len(pizzaManager.allValidSlicePaths))
	i = 1
	for slicePath in pizzaManager.allValidSlicePaths:
		print("Current Slice Path: ", i)
		for slice in slicePath:
			print(" ".join([str(slice.startRow), str(slice.startCol), str(slice.endRow), str(slice.endCol)]))
		i += 1

	# for slice in pizzaManager.startSlices:
	# 	print("Before cutting the dish looks like this: \n", pizza.dish, end="\n")
	# 	print("Checking if we can actually cut the piece out...")
	# 	if pizzaManager.isValidSlice(Slice):
	# 		print("Here's the slice you cut out: \n", pizza.cut(slice), end="\n")
	# 		print("Here are the neigbouring cells: ")
	# 		cells = pizzaManager.neighbourCells(slice)
	# 		for cell in cells:
	# 			print((cell.startRow, cell.startCol), end="\n")
	# 	else:
	# 		print("Failed to cut! The space is not completely filled with pizza.")
	# 	print("Now the pizza dish looks like this: \n", pizza.dish, end="\n")

