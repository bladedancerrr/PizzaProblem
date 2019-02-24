import numpy as np

class Slice:

	startRow = 0
	startCol = 0
	endRow = 0
	endCol = 0

	def __init__(self, s_r, s_c, e_r, e_c):
		self.startRow = s_r
		self.startCol = s_c
		self.endRow = e_r
		self.endCol = e_c

	def extendLeft(self):
		self.startCol -= 1


	def extendRight(self):
		self.endCol += 1


	def extendUp(self):
		self.startRow -= 1 


	def extendDown(self):
		self.endRow += 1

	def display(self, pizza):
		paper = np.zeros(pizza.pizzaArray.shape, dtype=int)
		paper[self.startRow:self.endRow + 1, self.startCol:self.endCol + 1] = 1
		print(paper)

class Cell(Slice):

	def __init__(self, row, col):
		self.startRow = row
		self.startCol = col
		self.endRow = row
		self.endCol = col


if __name__ == "__main__":
	slice = Slice(0, 0, 2, 2)
	cell = Cell(2, 2)




 