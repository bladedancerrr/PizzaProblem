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
	print(shape)
	dimension_list = determineCutPoints((pizza.rows, pizza.cols), shape)
	slices = perform_actual_cutting(dimension_list)
	print("amount of slices: ", len(slices))
	i = 0
	for slice in slices:
		i += 1
		slice.display(pizza)
		print(is_validate_slice(pizza, slice))
		if is_validate_slice(pizza, slice):
			print("Valid")
		else:
			slices.remove(slice)
			print("Invalid")
	print(i)
	print_file(slices)


if __name__ == '__main__':
	inputFile = "inputFiles/a_example.in"
	main(inputFile)
