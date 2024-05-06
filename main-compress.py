from contextlib import closing
from General.Processor import Processor
from IO.FileOutput import FileOutput
from Image.LeftImage import LeftImage
from Image.UpperImage import UpperImage
from Image.MedianeImage import MedianeImage
from Image.ImageLoader import ImageLoader
from Context.DefaultContext import DefaultContext
from Distribution.Distribution import Distribution
from matplotlib import pyplot as plt
from General.Results import Results
from Distribution.EmptyDistributionError import EmptyDistributionError
import sys
import os
import time

startTime = time.time()

if len(sys.argv) != 3:
	print("Bad number of arguments")
	sys.exit(1)

nameOfImage = sys.argv[1]
stemOfImage = os.path.splitext(nameOfImage)[0]
kind = sys.argv[2]
classOfImage = ( LeftImage if kind == "left" else UpperImage if kind == "upper" else
	MedianeImage if kind == "mediane" else None )
image = ImageLoader.load(nameOfImage, classOfImage, DefaultContext)
with closing(FileOutput(stemOfImage + ".com")) as out:
	try:
		statistics, sizes = Processor.code(image, out)
		statistics.drawHistograms(stemOfImage, kind)
		Results.write(stemOfImage + "-results.txt", statistics, time.time() - startTime, sizes) 

	except EOFError:
		print("Input file too short", file = sys.stderr)
		sys.exit(1)
		
	except EmptyDistributionError as exc:
		print(exc, file = sys.stderr)
		sys.exit(2)
