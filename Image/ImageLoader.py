import cv2
import numpy as np

class ImageLoader:
	
	@staticmethod
	def empty(frame, cls, ctx):
		return cls(np.zeros((frame.height, frame.width)), ctx)
		
	@staticmethod
	def load(filename, cls, ctx):
		return cls(cv2.imread(filename, cv2.IMREAD_GRAYSCALE), ctx)
