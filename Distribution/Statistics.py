from Distribution.Distribution import Distribution
from Distribution.Histogram import Histogram
from matplotlib import pyplot as plt

class Statistics:

	def __init__(self, originalHistogram, predictionHistogram):
		self.originalHistogram = originalHistogram
		self.predictionHistogram = predictionHistogram
		self.originalDistribution = Distribution(originalHistogram)
		self.predictionDistribution = Distribution(predictionHistogram)
		
	def drawHistograms(self, filebase, which):
		for method in ( (Histogram.bar, "bar"), 
			(Histogram.plot, "plot"), (Histogram.step, "step")):
			plt.figure(figsize = (20, 10))
			plt.title("Original", fontsize = 40)
			plt.xticks(list(range(0, 270, 10)))
			method[0](self.originalHistogram, color = "b")
			plt.savefig(filebase + "-" + method[1] + "-original.png")
			plt.clf()
			plt.figure(figsize = (20, 10))
			plt.title(which.capitalize(), fontsize = 40)
			plt.xticks(list(range(-260, 280, 20)))
			method[0](self.predictionHistogram, color = "r")
			plt.savefig(filebase + "-" + method[1] + "-" + which + ".png")
			plt.clf()
