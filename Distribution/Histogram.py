from matplotlib import pyplot as plt

class Histogram:
	
	def __init__(self, line, scope):
		self.data = {}
		self.length = len(line)
		for x in scope:
			self.data[x] = 0
		for x in line:
			self.data[x] += 1
			
	def labels(self):
		plt.xlabel("Values", fontsize = 32)
		plt.ylabel("Occurences", fontsize = 32)
			
	def bar(self, color):
		plt.bar(list(self.data.keys()), list(self.data.values()), width = 1, color = color)
		self.labels()
		
	def plot(self, color):
		plt.plot(list(self.data.keys()), list(self.data.values()), color = color)
		self.labels()
		
	def step(self, color):
		plt.step(list(self.data.keys()), list(self.data.values()), color = color)
		self.labels()
