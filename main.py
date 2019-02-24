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
	for slice in slices:
		if not is_validate_slice(slice):
			slices.remove(slice)
	print_file(slices)


if __name__ == '__main__':
	inputFile = "inputFiles/a_example.in"
	main(inputFile)
