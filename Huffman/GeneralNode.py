class GeneralNode:

	def __init__(self, weight):
		self.weight = weight
		self.parent = None
		
	def setParent(self, parent, bit):
		self.parent = parent
		self.label = bit
		
	def route(self):
		if not self.parent:
			return []
		else:
			return self.parent.route() + [ self.label ]
			
	@staticmethod
	def sort(one):
		return one.weight
