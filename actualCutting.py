# written by Peter Shi
from sliceStructure import Slice


def perform_actual_cutting(dimension_list):
    horizontal_dimension = dimension_list[0]
    vertical_dimension = dimension_list[1]

    slice_list = list()

    assert len(horizontal_dimension) == len(vertical_dimension)
    for i in range(len(horizontal_dimension)):
        s_c = horizontal_dimension[i][0]
        e_c = horizontal_dimension[i][1]
        s_r = vertical_dimension[i][0]
        e_r = vertical_dimension[i][1]

        new_slice = Slice(s_r, s_c, e_r, e_c)
        slice_list.append(new_slice)
    return slice_list
