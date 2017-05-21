import numpy as np
import os
import sys

def return_shape(numpy_file):
	a=np.load(numpy_file)
	b=a.shape
	return b

list_shapes = []

def traverse_npy_dirs(dir_path):
	for directory,subdirectories,files in os.walk(dir_path):
		for file1 in files:
			j = os.path.join(directory,file1)
			print j
			filename,fileext=os.path.splitext(file1)
			if fileext == ".npy":
				print filename
				print fileext
				shape = return_shape(j)
				list_shapes.append(shape[1])
		print sum(list_shapes)

if __name__ == "__main__":
	if(len(sys.argv))!=2:
		print 'sum_npy.py input_dir_path'
	else:	
		traverse_npy_dirs(sys.argv[1])
