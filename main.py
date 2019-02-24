from pizzaStructure import Pizza
from sliceStructure import Slice
from validate_slice import is_validate_slice
from shapeMaker import pizzaShape
from writingFile import print_file
from determineCutPoints import determineCutPoints
from actualCutting import perform_actual_cutting

def main(fileName):
	pizza = Pizza(fileName)
	shape = pizzaShape(pizza)
	dimension_list = determineCutPoints((pizza.rows, pizza.cols), shape)
	slices = perform_actual_cutting(dimension_list)
	validSlices = []
	for slice in slices:
		print("Cut out this: ", pizza.cut(slice), "\n")
		print("From this pizza: ") 
		slice.display(pizza)
		print("\n")
		print("valid Slice? ", is_validate_slice(pizza, slice))
		if is_validate_slice(pizza, slice):
			validSlices.append(slice)
	print_file(validSlices)
	print("Covered ", (len(validSlices)*shape[0]*shape[1]/(pizza.rows*pizza.cols))*100, end=" %\n")


if __name__ == '__main__':
	fileNames = ["inputFiles/a_example.in", "inputFiles/b_small.in", "inputFiles/c_medium.in", "inputFiles/d_big.in"]
	inputFile = fileNames[3]
	main(inputFile)
