from Image.Image import Image
from Image.LeftImage import LeftImage
from Image.UpperImage import UpperImage
from Image.LeftUpperImage import LeftUpperImage

class MedianeImage(Image):

	def __init__(self, data, ctx):
		Image.__init__(self, data, ctx)
		self.left = LeftImage(data, ctx)
		self.upper = UpperImage(data, ctx)
		self.leftUpper = LeftUpperImage(data, ctx)
		
	def getPrevious(self, counter):
		return self.ctx.mediane(self.left.getPrevious(counter),
			self.upper.getPrevious(counter),
			self.leftUpper.getPrevious(counter))
