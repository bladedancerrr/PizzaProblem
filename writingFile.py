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

		
