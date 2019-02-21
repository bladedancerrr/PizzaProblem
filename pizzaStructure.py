class Pizza:

	# properties
	rows = 0
	cols = 0
	minOfEachIngredient = 0
	maxCells = 0

	pizzaDict = {}

	# this is run once only when we create the object
	def __init__(self, textFileName):
		"""
		:type textFileName: string

		This function takes a textFileName as input, finds that file in the same directory, processes it, 
		and updates the properties and pizzaDict

		sampleTextFile:
		3 5 1 6
		TTTTT
		TMMMT
		TTTTT
		"""

		### processing code goes here:

		textFile = self.textFile(textFileName)
		self.updateRCLH(textFile)
		self.updatePizzaDict(textFile)

		### testing is done here:

		self.testProperties()
		self.testPizzaDict()



	### processing functions written here
	
	def textFile(self, textFileName):
		"""
		returns a python text file from the directory
		"""
		pass

	def updateRCLH(self, textFile):
		"""
		grab the data from the textFile and update the properties
		"""

		#sample values that need to be updated
		self.rows = 2
		self.cols = 5
		self.minOfEachIngredient = 1
		self.maxCells = 6

	def updatePizzaDict(self, textFile):
		"""
		grab the data from the textFile and update pizzaDict
		"""

		# this is tricky, coz you gotta change all the T to 1 ; M to 0 then put them into the pizzaDict
		self.pizzaDict = {0: [1, 1, 1, 1, 1], 1: [1, 0, 0, 0, 1], 2: [1, 1, 1, 1, 1]}



	### testing functions written here

	#Lexon's note: we can use Ayesha's test library

	def testRows(self):
		# example
		assert self.rows >= 1 and self.rows <= 1000, "Rows out of bounds!"

	def testCols(self):
		pass

	def testMinOfEachIngredient(self):
		pass

	def testMaxCells(self):
		pass

	def testProperties(self):
		self.testRows()
		self.testCols()
		self.testMinOfEachIngredient()
		self.testMaxCells()
		print("Properties tests passed!")

	def testPizzaDict(self):
		print(len(self.pizzaDict.keys()), self.rows)
		assert len(self.pizzaDict.keys()) == self.rows, "What the hell?! Number of keys should equal number of rows!"
		for row in self.pizzaDict.values():
			assert len(row) == self.cols, "Hey!! Number of items in list should equal number of columns!"
		print("PizzaDict test passed!")



pizza = Pizza("someTextFileName")

# Processing and testing done. We can use now! Yay!
print("Number of rows of the Pizza: ", pizza.rows)
print("The pizza looks like this: ", pizza.pizzaDict)