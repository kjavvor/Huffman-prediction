class Coder:

	def __init__(self, terminals):
		self.terminals = terminals
		
	def code(self, symbol):
		return self.terminals[symbol].route()
		
	def codeLine(self, symbols):
		result = []
		for symbol in symbols:
			result += self.code(symbol)
		return result
