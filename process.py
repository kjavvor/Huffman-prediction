import subprocess
import shutil
import os
	
base = "Solution"

for source in ( "Pictures", "Distributions" ):
	for picture in os.listdir(source):
		basename = os.path.splitext(picture)[0]
		for trybe in ( "left", "upper", "mediane" ):
			directory = os.path.join(base, source, basename, trybe)
			if not os.path.exists(directory):
				os.makedirs(directory)
			shutil.copyfile(os.path.join(source, picture) , os.path.join(directory, picture)) 
			for app in ( ("main-compress.py", "pgm"), ("main-decompress.py", "com") ):
				subprocess.run(["python3", app[0], os.path.join(directory, basename) + "." + app[1], trybe])
