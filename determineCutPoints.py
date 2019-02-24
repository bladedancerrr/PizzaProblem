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

	startPoint = 0
	endPoint = lSlice - 1

	while endPoint < l:
		horizontalPoints.append([startPoint, endPoint])
		startPoint = endPoint + 1
		endPoint = startPoint + lSlice - 1

	startPoint = 0
	endPoint = hSlice - 1

	while endPoint < h:
		for i in range(len(horizontalPoints)):
			verticalPoints.append([startPoint, endPoint])
		startPoint = endPoint + 1
		endPoint = startPoint + hSlice - 1

	return [horizontalPoints, verticalPoints]



print(determineCutPoints((3, 5),(2, 1)))