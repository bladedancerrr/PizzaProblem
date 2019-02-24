# written by Peter Shi
from sliceStructure import Slice


def perform_actual_cutting(dimension_tuple):
    horizontal_dimension = dimension_tuple[0]
    vertical_dimension = dimension_tuple[1]

    slice_list = list()

    assert len(horizontal_dimension) == len(vertical_dimension)
    for i in range(len(horizontal_dimension)):
        s_r = horizontal_dimension[i][0]
        e_r = horizontal_dimension[i][0]
        s_c = vertical_dimension[i][0]
        e_c = vertical_dimension[i][0]

        new_slice = Slice(s_r, s_c, e_r, e_c)
        slice_list.append(new_slice)
    return slice_list
