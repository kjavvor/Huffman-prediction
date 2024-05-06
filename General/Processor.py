from Frame.FrameCounter import FrameCounter
from Distribution.Distribution import Distribution
from Huffman.HuffmanGenerator import HuffmanGenerator
from Bits.Packer import Packer
from Image.ImageLoader import ImageLoader
import Huffman.Decoder
from Sizes.Sizes import Sizes
from Distribution.Statistics import Statistics
from Distribution.Histogram import Histogram

class Processor:

	@staticmethod
	def code(image, out):
		frame = image.frame()
		out.writeFrame(frame)
		counter = FrameCounter(frame)
		coding = []
		while counter:
			coding.append(image[counter])
			counter.advance()
		statistics = Statistics(Histogram(image.flatten(), range(256)),
			Histogram(coding, range(-255, 256)))
		coder, root, statistics.average = (
			HuffmanGenerator().generateBasedOnDistribution(statistics.predictionDistribution) )
		treeSize = out.writeObject(root)
		arraySize = out.writeArray(Packer.pack(coder.codeLine(coding)))
		return statistics, Sizes(image.size(), treeSize, arraySize)
		
	@staticmethod
	def decode(inp, imageClass, ctx):
		frame = inp.readFrame()
		image = ImageLoader.empty(frame, imageClass, ctx)
		counter = FrameCounter(frame)
		decoder = Huffman.Decoder.Decoder(inp.readObject())
		bits = Packer.unpack(inp.readArray())
		position = 0
		while counter:
			image[counter], position = decoder.decode(bits, position)
			counter.advance()
		return image
