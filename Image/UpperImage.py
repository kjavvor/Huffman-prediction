from Image.Image import Image

class UpperImage(Image):

	def lower(self, counter):
		return counter.x, counter.y - 1
