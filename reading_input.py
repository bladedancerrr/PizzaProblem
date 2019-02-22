import numpy as np
import matplotlib.pyplot as plt


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
    R, C, L, H = [int(val) for val in lines[0].split()]
    pizza = np.array([list(map(lambda item: 1 if item == 'T' else 0, row.strip())) for row in lines[1:]])
    print(pizza)


R, C, L, H, pizza = read_input_pizza('/home/ayesha/GoogleHashCode/inputFiles/a_example.in')

# fig, ax = plt.subplots()
# ax.imshow(pizza)
# ax.set_title(f'medium.in shape is {pizza.shape}, max. score {pizza.size}\nmin. ingredients is {L}, max. piza slice is {H}');
# plt.show()

