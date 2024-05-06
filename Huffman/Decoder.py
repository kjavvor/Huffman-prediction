from Huffman.Terminal import Terminal

class Decoder:

	def __init__(self, root):
		self.last = self.root = root
		
	def rewind(self):
		self.last = self.root
		
	def savePosition(self, node):
		self.last = node
		return isinstance(node, Terminal)
		
	def advance(self, bit):
		return self.last.trace(bit, self)
	
	def decode(self, bits, position):
		return self.root.trace(bits, position)
	
	def simple(self):
		return isinstance(self.root, Terminal)
