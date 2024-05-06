from Image.Image import Image

class LeftImage(Image):

	def lower(self, counter):
		return counter.x - 1, counter.y
