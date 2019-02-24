def is_validate_slice(pizza, a_slice, min_ingredients):
    number_of_tomato = 0

    for i in range(a_slice.startRow, a_slice.endRow + 1):
        for j in range(a_slice.startCol, a_slice.endCol + 1):
            cell = pizza.pizzaArray[i][j]
            number_of_tomato += cell

    number_of_cells = get_slice_size(a_slice)
    number_of_mushroom = number_of_cells - number_of_tomato

    return (number_of_tomato >= min_ingredients) and (number_of_mushroom >= min_ingredients)


def get_slice_size(slice):
    return (slice.endRow - slice.startRow) * (slice.endCol - slice.startCol)