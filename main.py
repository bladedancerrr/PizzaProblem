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
	for i in range(len(slices)):
		slices[i].display(pizza)
		print(is_validate_slice(pizza, slices[i]))
		if is_validate_slice(pizza, slices[i]):
			print("Valid")
		else:
			slices.remove(slices[i])
			print("Invalid")
			
	print("Times run: ", i)
	print_file(slices)


if __name__ == '__main__':
	inputFile = "inputFiles/a_example.in"
	main(inputFile)
