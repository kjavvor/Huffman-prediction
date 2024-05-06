import math
from matplotlib import pyplot as plt

class Distribution:

	def __init__(self, histogram):
		self.data = {}
		for x, y in histogram.data.items():
			self.data[x] = y / histogram.length
				
	def __iter__(self):
		return iter(self.data.items())
		
	def countEntropy(self):
		return - sum([ p * math.log(p, 2) for p in self.data.values() if p != 0 ])
		
	def countAverageOfHuffman(self, terminals):
		return sum([ self.data[symbol] * len(terminal.route())
			for symbol, terminal in terminals.items() ]) 
		
	def empty(self):
		return len(self.data) == 0
