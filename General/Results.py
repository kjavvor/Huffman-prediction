class Results:

	@staticmethod
	def write(filename, statistics, time, sizes):
		with open(filename, "w") as handle:
			handle.write("Entropy of original data: %.3f\n" % 
				statistics.originalDistribution.countEntropy())
			handle.write("Entropy of prediction data: %.3f\n" % 
				statistics.predictionDistribution.countEntropy())
			handle.write("Average length of word: %.3f bits\n" % statistics.average)
			handle.write("Size of original image data: %d bytes\n" % sizes.imageSize)
			handle.write("Size of encoded Huffman tree: %d bytes\n" % sizes.treeSize)
			handle.write("Size of encoded data: %d bytes\n" % sizes.arraySize)
			handle.write("Compressed/Original ratio: %.3f\n" % (sizes.arraySize / sizes.imageSize))
			handle.write("Time of compression: %.3fs\n" % time)
			
	def writeDecompressionTime(filename, time):
		with open(filename, "a") as handle:
			handle.write("Time of decompression: %.3fs\n" % time)
