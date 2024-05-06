import pickle

class FileOutput:

	def __init__(self, filename):
		self.handle = open(filename, "wb")
	
	def close(self):
		self.handle.close()
			
	def writeNumber(self, number):
		self.handle.write(number.to_bytes(4, "little"))
		
	def writeArray(self, array):
		length = len(array)
		self.writeNumber(length)
		self.handle.write(array)
		return length
	
	def writeObject(self, obj):
		return self.writeArray(pickle.dumps(obj))
		
	def writeFrame(self, frame):
		self.writeNumber(frame.width)
		self.writeNumber(frame.height)
		
