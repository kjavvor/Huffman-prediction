class Generator:

	def generateBasedOnFragment(self, fragment):
		weights = {}
		for symbol in fragment:
			if symbol in weights:
				weights[symbol] += 1
			else:
				weights[symbol] = 1
		return self.generateBasedOnWeights(weights)
