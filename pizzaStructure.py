class Pizza:

	# properties
	rows = 0
	cols = 0
	minOfEachIngredient = 0
	maxCells = 0
	isValidSlice = True

	pizzaDict = {}

	# this is run once only when we create the object
	def __init__(self, fileName=None):
		assert filename!=None "Please input file name." 
		"""
		:type textFileName: string

		This function takes a textFileName as input, finds that file in the same directory, processes it, 
		and updates the properties and pizzaDict
		"""

		### processing code goes here:

		lines = self.textFile(fileName)
		self.updateRCLH(lines)
		self.updatePizzaDict(lines)

		### testing is done here:

		self.testProperties()
		self.testPizzaDict()



	### processing functions written here
	
	def textFile(self, fileName):
		"""
		returns a python text file from the directory
		"""
		lines = open(fileName).readlines()
		return lines
	    
	def updateRCLH(self, lines):
		"""
		grab the data from the textFile and update the properties
		"""
		self.rows, self.cols, self.minOfEachIngredient, self.maxCells = [int(val) for val in lines[0].split()]

	def updatePizzaDict(self, lines):
		"""
		grab the data from the textFile and update pizzaDict
		"""
		key = 0
		for row in lines[1:]:
			self.pizzaDict[key] = list(map(lambda item: 1 if item == 'T' else 0, row.strip()))
			key += 1


	### testing functions written here

	def testRows(self):
		assert self.rows >= 1 and self.rows <= 1000, "Rows out of bounds!"

	def testCols(self):
		assert self.cols >= 1 and self.cols <= 1000, "Rows out of bounds!"

	def testMinOfEachIngredient(self):
		assert self.minOfEachIngredient >= 1 and self.minOfEachIngredient <= 1000, "Rows out of bounds!"

	def testMaxCells(self):
		assert self.maxCells >= 1 and self.maxCells <= 1000, "Rows out of bounds!"


	def testProperties(self):
		self.testRows()
		self.testCols()
		self.testMinOfEachIngredient()
		self.testMaxCells()
		print("Properties tests passed!")

	def testPizzaDict(self):
		assert len(self.pizzaDict.keys()) == self.rows, "What the hell?! Number of keys should equal number of rows!"
		for row in self.pizzaDict.values():
			assert len(row) == self.cols, "Hey!! Number of items in list should equal number of columns!"
		print("PizzaDict test passed!")


	def isValidSlice(self):
		return self.rows * self.cols <= self.maxCells

pizza = Pizza("inputFiles/a_example.in")

# Processing and testing done. We can use now! Yay!
print("Number of rows of the Pizza: ", pizza.rows)
print("The pizza looks like this: ", pizza.pizzaDict)