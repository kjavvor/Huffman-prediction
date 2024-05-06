from contextlib import closing
from General.Processor import Processor
from IO.FileInput import FileInput
from Image.LeftImage import LeftImage
from Image.UpperImage import UpperImage
from Image.MedianeImage import MedianeImage
from Image.ImageLoader import ImageLoader
from Context.DefaultContext import DefaultContext
from General.Results import Results
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

with closing(FileInput(nameOfImage)) as inp:
	try:
		Processor.decode(inp, classOfImage, DefaultContext).save(stemOfImage + "-re.pgm")
		Results.writeDecompressionTime(stemOfImage + "-results.txt", time.time() - startTime)
	except EOFError:
		print("Input file too short", file = sys.stderr)
		sys.exit(1)
