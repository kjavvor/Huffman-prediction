import pickle
from Frame.Frame import Frame

class FileInput:

	def __init__(self, filename):
		self.handle = open(filename, "rb")
		
	def close(self):
		self.handle.close()
		
	def readNumber(self):
		length = 4
		score = self.handle.read(length)
		if len(score) != length:
			raise EOFError()
		return int.from_bytes(score, "little")
		
	def readArray(self):
		length = self.readNumber()
		score = self.handle.read(length)
		if len(score) != length:
			raise EOFError()
		return score
		
	def readObject(self):
		return pickle.loads(self.readArray())
		
	def readFrame(self):
		return Frame(self.readNumber(), self.readNumber())
			
		
	
