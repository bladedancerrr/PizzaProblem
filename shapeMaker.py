from pizzaStructure import Pizza

def pizzaShape(pizza):
	startSlices = []
	minSizeOfSlice = pizza.L * 2
	col = minSizeOfSlice
	row = 1
	combinations = []
	while col % 2 == 0:
		combinations.append((row, col))
		col = col//2
		row = minSizeOfSlice//col

	maxDiff = abs(combinations[0][0] - combinations[0][1])
	maxDiffComboNumber = 0
	for comboNumber in range(len(combinations)):
		diff = abs(combinations[comboNumber][0] - combinations[comboNumber][1])
		if diff > maxDiff:
			maxDiff = diff
			maxDiffComboNumber = comboNumber
	return combinations[comboNumber]

if __name__ == "__main__":
	pizza = Pizza("inputFiles/a_example.in")
	print(pizzaShape(pizza))