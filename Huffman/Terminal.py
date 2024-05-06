from Huffman.GeneralNode import GeneralNode

class Terminal(GeneralNode):

	def __init__(self, symbol, weight):
		GeneralNode.__init__(self, weight)
		self.symbol = symbol
	
	def trace(self, bits, position):
		return self.symbol, position
