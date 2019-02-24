from sliceStructure import Slice

def print_file(slices):
	"""
	This function creates an output file
	of the correct format from the slices
	"""
	f = open("Output.txt", 'w') #opening file as f in writing mode
	f.write(f"{len(slices)}\n") #number of slices in slices list
	for slice in slices:
		f.write(f"{slice.startRow} {slice.startCol} {slice.endRow} {slice.endCol}\n")

		
if __name__ == "__main__":
    a = Slice(0, 0, 2, 2)
    b = Slice(3, 3, 5, 5)
    c = Slice(6, 6, 8, 8)

    print_file([a, b, c])
