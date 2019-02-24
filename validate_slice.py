from pizzaStructure import Pizza
from sliceStructure import Slice

def is_validate_slice(pizza, a_slice):
    number_of_tomato = 0

    for i in range(a_slice.startRow, a_slice.endRow + 1):
        for j in range(a_slice.startCol, a_slice.endCol + 1):
            cell = pizza.pizzaArray[i][j]
            number_of_tomato += cell

    number_of_cells = get_slice_size(a_slice)
    number_of_mushroom = number_of_cells - number_of_tomato

    return (number_of_tomato >= pizza.L) and (number_of_mushroom >= pizza.L)



def get_slice_size(slice):
    return (slice.endRow - slice.startRow + 1) * (slice.endCol - slice.startCol + 1)


if __name__ == '__main__':
	pizza = Pizza("inputFiles/a_example.in")
	slice = Slice(0, 0, 2, 2)
	slice.display(pizza)
	print("************")
	print(pizza.cut(slice))
	print(is_validate_slice(pizza, slice))