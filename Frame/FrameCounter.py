class FrameCounter:

	def __init__(self, frame):
		self.frame = frame
		self.x = 0
		self.y = 0
		
	def advance(self):
		self.x += 1
		if self.x == self.frame.width:
			self.x = 0
			self.y += 1
			
	def __bool__(self):
		return self.y != self.frame.height
