def read_input_pizza(filename):
    """Reads the input of a Pizza problem.

    returns:

    R: number of Rows of pizza grid
    C: number of Cols of pizza grid
    L: Lowest number of each ingredients per slice
    H: Highest number of cells per slice
    pizza: the pizza grid (1 == tomato, 0 == mushroom)
    """
    lines = open(filename).readlines()
    print(type(lines))
    R, C, L, H = [int(val) for val in lines[0].split()]
    pizza = [list(map(lambda item: 1 if item == 'T' else 0, row.strip())) for row in lines[1:]]
    return R, C, L, H, pizza

read_input_pizza('inputFiles/a_example.in')

#test code
# R, C, L, H, pizza = read_input_pizza('inputFiles/a_example.in')
# print(R, C, L, H)
# print(pizza)

