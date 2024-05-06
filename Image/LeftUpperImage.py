from Image.Image import Image

class LeftUpperImage(Image):

	def lower(self, counter):
		return counter.x - 1, counter.y - 1
