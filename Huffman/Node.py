from Huffman.GeneralNode import GeneralNode

class Node(GeneralNode):
	
	def __init__(self, left, right):
		GeneralNode.__init__(self, left.weight + right.weight)
		left.setParent(self, 0)
		right.setParent(self, 1)
		self.left = left
		self.right = right
		
	def trace(self, bits, position):
		if bits[position] == 0:
			return self.left.trace(bits, position + 1)
		else:
			return self.right.trace(bits, position + 1)
			
	def decode(self):
		pass
