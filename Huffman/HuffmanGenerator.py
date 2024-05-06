from Huffman.Generator import Generator
from Huffman.GeneralNode import GeneralNode
from Huffman.Coder import Coder
from Huffman.Decoder import Decoder
from Huffman.Terminal import Terminal
from Huffman.Node import Node
from Distribution.EmptyDistributionError import EmptyDistributionError

class HuffmanGenerator(Generator):

	def generateBasedOnDistribution(self, distribution):
		if distribution.empty():
			raise EmptyDistributionError
		nodes = []
		terminals = {}
		for symbol, weight in distribution:
			if weight != 0:
				terminal = Terminal(symbol, weight)
				terminals[symbol] = terminal
				nodes.append(terminal)
		while len(nodes) >= 2:
			nodes.sort(key = GeneralNode.sort)
			nodes.append(Node(nodes[0], nodes[1]))
			nodes[:2] = []
		return Coder(terminals), nodes[0], distribution.countAverageOfHuffman(terminals)
