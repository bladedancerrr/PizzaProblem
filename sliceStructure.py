class Slice:

	start_r = 0
	start_c = 0
	end_r = 0
	end_c = 0

	def __init__(self, s_r, s_c, e_r, e_c):
		self.start_r = s_r
		self.start_c = s_c
		self.end_r = e_r
		self.end_c = e_c

	def extendLeft(self):
		self.start_c -= 1


	def extendRight(self):
		self.end_c += 1


	def extendUp(self):
		self.start_r -= 1 


	def extendDown(self):
		self.end_r += 1
 