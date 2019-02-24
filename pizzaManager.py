from pizzaStructure import Pizza
from sliceStructure import Slice, Cell
import numpy as np
# list of slices


class PizzaManager:
	def __init__(self, pizza):
		self.pizza = pizza
		self.allValidSlicePaths = []

	def startSlices(self, startCell):
		startSlices = []
		minSizeOfSlice = self.pizza.L * 2
		col = minSizeOfSlice
		row = 1
		combinations = []
		while col % 2 == 0:
			combinations.append((row, col))
			col = col//2
			row = minSizeOfSlice//col

		for combo in combinations:
			slice = Slice(startCell.startRow, startCell,startCol, combo[0] - 1, combo[1] - 1)
			if self.isValidSlice(Slice):
				startSlices.append(slice)

		for combo in combinations:
			slice = Slice(startCell.startRow, startCell.startCol, combo[1] - 1, combo[0] - 1)
			if self.isValidSlice(Slice):
				startSlices.append(slice)
			
		return startSlices

	def isValidSlice(self, slice):
		for row in range(slice.startRow, slice.endRow + 1):
			for col in range(slice.startCol, slice.endCol + 1):
				if row < 0 or row > self.pizza.rows - 1 or col < 0 or col > self.pizza.cols - 1 or self.pizza.dish[row, col] == 1:
					return False
		return True

	def neighbourCells(self, slice):
		cells = []
		# on the left
		for row in range(slice.startRow, slice.endRow + 1):
			cell = Cell(row, slice.startCol - 1)
			if self.isValidSlice(cell):
				cells.append(cell)

		# on right
		for row in range(slice.startRow, slice.endRow + 1):
			cell = Cell(row, slice.endCol + 1)
			if self.isValidSlice(cell):
				cells.append(cell)

		# on top
		for col in range(slice.startCol, slice.endCol + 1):
			cell = Cell(slice.startRow - 1, col)
			if self.isValidSlice(cell):
				cells.append(cell)

		# on bottom
		for col in range(slice.startCol, slice.endCol + 1):
			cell = Cell(slice.endRow + 1, col)
			if self.isValidSlice(cell):
				cells.append(cell)

		return cells


	def allPossibleValidSlicePaths(self):
		startSlices = self.startSlices(Cell(0, 0))
		for slice in startSlices:
			slicePaths = [[slice]]
			i = 0
			for cell in self.neighbourCells(slice):
				slicePaths


if __name__ == "__main__":
	pizza = Pizza("inputFiles/a_example.in")
	pizzaManager = PizzaManager(pizza)
	for slice in pizzaManager.startSlices:
		print("Before cutting the dish looks like this: \n", pizza.dish, end="\n")
		print("Checking if we can actually cut the piece out...")
		if pizzaManager.isValidSlice(Slice):
			print("Here's the slice you cut out: \n", pizza.cut(slice), end="\n")
			print("Here are the neigbouring cells: ")
			cells = pizzaManager.neighbourCells(slice)
			for cell in cells:
				print((cell.startRow, cell.startCol), end="\n")
		else:
			print("Failed to cut! The space is not completely filled with pizza.")
		print("Now the pizza dish looks like this: \n", pizza.dish, end="\n")

