import numpy as np
import os
import sys
import random
import argparse
from collections import Counter

def create_train_test_validate(input_list_file,audio_feat_list,output_root):
	input_list_filename = input_list_file.split('/')[-1].replace(' ','_').split('.txt')[0]
	random.seed(2017)
	lines = open(input_list_file).readlines()
	audiopairlines = open(audio_feat_list).readlines()
	random.shuffle(lines)
	print audiopairlines
	filenames_array = []
	classnames_array = []
	training_set = []
	testing_set = []
	validation_set = []
	training_set_label = []
	testing_set_label = []
	validation_set_label = []
	ratio = [3,1,1]
	for i in range(len(lines)):
		a= lines[i].strip()
		classname = a.split('\t')[0]
		filenames = a.split('\t')[1]
		filenames_array.append(filenames)
		classnames_array.append(classname)
	counter_dict = Counter(classnames_array)
	counter_new = counter_dict.most_common()
	for j,x in enumerate(counter_new):
		indices = [i for i, class_name in enumerate(classnames_array) if class_name == x[0]]		
		validation_indices = indices[:(len(indices)/5)]
		testing_indices  = indices[(len(indices)/5):(2*len(indices)/5)]
		training_indices = indices[(2*len(indices)/5):]
		training_file = [filenames_array[i] + ',' + x[0] for i in training_indices]
		training_file_label = [filenames_array[i] + ',' + str(j) for i in training_indices]
		testing_file = [filenames_array[i] + ',' + x[0] for i in testing_indices]
		testing_file_label = [filenames_array[i] + ',' + str(j) for i in testing_indices]
		validation_file = [filenames_array[i] + ',' + x[0] for i in validation_indices]
		validation_file_label = [filenames_array[i] + ',' + str(j) for i in validation_indices]
		training_set.extend(training_file)
		testing_set.extend(testing_file)
		validation_set.extend(validation_file)
		training_set_label.extend(training_file_label)
		testing_set_label.extend(testing_file_label)
		validation_set_label.extend(validation_file_label)
	if not os.path.exists(output_root):
		os.makedirs(output_root)
	training_file = output_root + '/' + input_list_filename + '_training.list'
	testing_file = output_root + '/' + input_list_filename + '_testing.list'
	validation_file = output_root + '/' + input_list_filename + '_validation.list'
	training_file_label = output_root + '/' + input_list_filename + '_training_label.list'
	testing_file_label = output_root + '/' + input_list_filename + '_testing_label.list'
	validation_file_label = output_root + '/' + input_list_filename + '_validation_label.list'
	counter_file = output_root + '/' + input_list_filename + 'counter.list'
	print training_file
	print testing_file
	print validation_file
	with open(training_file,'w') as f:
		for item in training_set:
			f.write(item + '\n')
	f.close()
	with open(testing_file,'w') as f:
		for item in testing_set:
			f.write(item + '\n')
	f.close()
	with open(validation_file,'w') as f:
		for item in validation_set:
			f.write(item + '\n')
	f.close()
	with open(training_file_label,'w') as f:
		for item in training_set_label:
			f.write(item + '\n')
	f.close()
	with open(testing_file_label,'w') as f:
		for item in testing_set_label:
			f.write(item + '\n')
	f.close()
	with open(validation_file_label,'w') as f:
		for item in validation_set_label:
			f.write(item + '\n')
	f.close()
	with open(counter_file,'w') as f:
		for item in counter_new:
			item = list(item)
			print item
			f.write(item[0] + ',' + str(item[1]) + '\n')
	f.close()

if __name__ == "__main__":
    print len(sys.argv)
    if len(sys.argv) != 7:
        print 'Takes arg1 = input-file mapping containing audiofile and class information, arg2 = audio_file_feature_list, arg3 = output list path'
    else:
	#Parameters hard coded as our paths remains fixed and less hassle changing parameters 
	parser = argparse.ArgumentParser()
	#print parser
	parser.add_argument('--input_file_list', type=str, default='mapping.list', metavar='N',
        	            help='input_file_list (default: mapping.list)')
	parser.add_argument('--audio_feat_list', type=str, default='features_file.list', metavar='N',
        	            help='audio_feat_list - default:features_file.list')
	parser.add_argument('--output_list_path', type=str, default='outputpath', metavar='N',
        	            help='output_list_path - default:outputpath')
	args = parser.parse_args()	
	## output path = os.getcwd + features/melspectrogram + sys.argv[2]
	## audio path = os.getcwd + audio + sys.argv[2]
	## output features = os.getcwd + audio
	output_list_root = args.output_list_path
	if not os.path.exists(output_list_root):
		os.makedirs(output_list_root)
	input_list_file = args.input_file_list
	audio_feat_list = args.audio_feat_list
	output_root = args.output_list_path
	print input_list_file
	print audio_feat_list
	print output_root
	create_train_test_validate(input_list_file,audio_feat_list,output_root)

#Sample command 
#python train_test_split.py  --input_file_list ../../audio/lists/original/clean_data.list --audio_feat_list ../../audio/original/clean_data/ --output_list_path ../../features/melspectrogram/original/clean_data 

