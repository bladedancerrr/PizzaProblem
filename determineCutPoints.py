def determineCutPoints(dimension, size):
	"""
	This function gets the height and length respectively
	of the pizza as 2-element tuple of integers (h,l)
	and calculates the cut sizes that will be made
	on the pizza and returns a tuple of lists 
	with the horizontal points and vertical points

	Input example: [(2, 2)]
	Output example: ([[0,1],[2,3]...[l-1,l]],[[0,1]),[2,3]...[h-1, h]])

	"""
	h = dimension[0] #height of pizza
	l =  dimension[1] #length of pizza

	hSlice = size[0] #height of required slice
	lSlice = size[1] #length of required slice

	horizontalPoints = [] 
	verticalPoints = []

	horizontalPoints.append([0, lSlice - 1])
	verticalPoints.append([0, hSlice -1])
	for i in range(1, l//lSlice):
		horizontalPoints.append(list(map(lambda x: x+lSlice, horizontalPoints[i - 1])))
	for j in range(1, h//hSlice):
		verticalPoints.append(list(map(lambda x: x+hSlice, verticalPoints[j - 1])))

	print(horizontalPoints, verticalPoints)



determineCutPoints((20,20),(15,15))