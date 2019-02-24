from pizzaStructure import Pizza

def pizzaShape(pizza):
	startSlices = []
	minSizeOfSlice = pizza.L * 2
	maxSizeOfSlice = pizza.H
	col = maxSizeOfSlice
	row = 1
	combinations = []
	combinations.append((row, col))

	while col % 2 == 0:
		col = col//2
		row = maxSizeOfSlice//col
		combinations.append((row, col))

	minDiff = abs(combinations[0][0] - combinations[0][1])
	minDiffComboNumber = 0
	for comboNumber in range(len(combinations)):
		diff = abs(combinations[comboNumber][0] - combinations[comboNumber][1])
		if diff < minDiff:
			minDiff = diff
			minDiffComboNumber = comboNumber
	return combinations[minDiffComboNumber]

if __name__ == "__main__":
	pizza = Pizza("inputFiles/a_example.in")
	print(pizzaShape(pizza))