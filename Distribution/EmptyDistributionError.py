class EmptyDistributionError(Exception):
	
	def __init__(self):
		Exception.__init__(self, 
			"A distribution used to build Huffman tree is empty")
