from bitstring import BitArray
from Bits.Bits import Bits

class Packer:

	@staticmethod
	def pack(bits):
		return BitArray(bits).tobytes()
		
	@staticmethod
	def unpack(line):
		return Bits.fromBitArray(BitArray(bytes = line))
