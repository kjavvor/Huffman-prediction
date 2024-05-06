import cv2
from Frame.Frame import Frame

class Image:

	def __init__(self, data, ctx):
		self.data = data
		self.ctx = ctx
		
	def save(self, filename):
		cv2.imwrite(filename, self.data)
		
	def __getitem__(self, counter):
		return int(self.getCurrent(counter)) - int(self.getPrevious(counter))
		
	def __setitem__(self, counter, difference):
		self.setCurrent(counter, self.getPrevious(counter) + difference)
		
	def getCurrent(self, counter):
		return self.data[counter.y, counter.x]
		
	def setCurrent(self, counter, value):
		self.data[counter.y, counter.x] = value
		
	def getPrevious(self, counter):
		x, y = self.lower(counter)
		if x < 0 or y < 0:
			return self.ctx.null()
		return self.data[y, x]
		
	def flatten(self):
		return self.data.flatten()
		
	def frame(self):
		shape = self.data.shape
		return Frame(shape[1], shape[0])
	
	def size(self):
		return self.data.size
