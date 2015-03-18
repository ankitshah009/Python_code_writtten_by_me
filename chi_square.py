import os
import re
import sys
import math

from sys import argv
#K(x,y)= 1-2*sum( (xi-yi)^2/(xi+yi)); # normal CHI^2


def chi_sq (x1,x2):      # x1, x2 must start from 1 to dimension i.e. exclude 0
	dim= len(x1)
	if dim != len(x2):
		return -1   #Invalid

	
	sum = 0.0
	#print "Param 1" + str(x1) + "Param 2" + str(x2)
	for i in range(0, dim):
		if(x1[i] + x2[i] == 0):
			continue	
		sum = sum + (math.pow((x1[i] -x2[i]),2)/(x1[i] +x2[i]))
		
	
	val = 1 - 2 * sum
	return val
"""
with open("train_data.txt","w") as userfile:
	for i in range(1,100):
		if (i%2 == 0):
			userfile.write("+1 ")
		else:
			userfile.write("-1 ")
		for j in range(1,10):
			userfile.write(str(i*j) + " ")
		userfile.write("\n")
	userfile.close()
"""
def chi_square_matric_generate(train_file_path, chi_square_output_folder):
	count = 0
	with open(train_file_path, "r") as userfile:
		line = userfile.readline()
		k=[]
		k=re.split(" |\n", line)
		data = re.split(" |\n", line)[1:len(k)]
		count = 0
		for item in data:
			if (''!=item):
				count = count+1
		#print count
	userfile.close()
		
	with open(train_file_path, "r") as userfile:
		data = []
		my_hist = []
		my_label = []
		
		for line in userfile:
			k=[]
			k=re.split(" |\n", line)	
			my_label.append(re.split(" |\n", line)[0])			
			data = re.split(" |\n", line)[1:]
			data2 = [0] * 200
			
			for item in data:
				if item == '':
					break
				if item == '\n':
					break
				feature = int(item.split(":")[0])
				value = float(item.split(":")[1])
				data2[feature] = value
			#print data2				
			my_hist.append(data2)
		
		userfile.close()
        if not os.path.exists(str(chi_square_output_folder)):
    		os.makedirs(str(chi_square_output_folder))
		
	
	
	with open(str(chi_square_output_folder) + "/chi_square_matrix.txt", "w") as userfile:
				
		global_count = 1			
		for item in my_hist:
			if(my_label[global_count-1] == '+1'):
				userfile.write("1 0:" + str(global_count) + " ")
			else:
				userfile.write("0 0:" + str(global_count) + " ")
			local_count = 0
			for i in range(0, len(my_hist)):
				local_count = local_count + 1
				#print i
				#print "call"
				sim = chi_sq(item, my_hist[i])
				#print sim
				userfile.write(str(local_count) + ":" + str(sim) + " ")
				
			global_count = global_count + 1
			userfile.write("\n")
		userfile.close()
		
print len(argv)
if(len(argv)!=3):
	print "USAGE: python chi_square.py <train_file_path> <chi_square_output_folder>"
else:
	train_file_path = ""
	train_file_path = argv[1]
	chi_square_output_folder = ""
	chi_square_output_folder = argv[2]
	chi_square_matric_generate(train_file_path, chi_square_output_folder)
