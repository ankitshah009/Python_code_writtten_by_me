#Original motivation behind code - http://stackoverflow.com/questions/16325258/numpyfinding-difference-between-two-files-containing-float-values
import numpy as np
import sys

def compare_numpy(input_file1,input_file2):
	file1=np.load(input_file1)
	file2=np.load(input_file2)
	threshold=float(1e-7)
	index_list = np.where(np.abs(file1-file2) > threshold)[0]
	for index in index_list:
		print (index,file1[index],file2[index])


if __name__ == "__main__":
	if len(sys.argv) !=3:
		print "python numpy_compare - first filepath, second absollute filepath"
	else:
		input_file1=sys.argv[1]
		input_file2=sys.argv[2]
		compare_numpy(input_file1,input_file2)
