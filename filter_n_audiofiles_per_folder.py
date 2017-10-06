import os,sys,subprocess,shutil

def copyFile(src, dest):
    try:
        shutil.copy(src, dest)
    # eg. src and dest are the same file
    except shutil.Error as e:
        print('Error: %s' % e)
    # eg. source or destination doesn't exist
    except IOError as e:
        print('Error: %s' % e.strerror)

def filter_n_audio(original_web_audio_dir,formatted_output_web_audio_dir,num_files_to_filter):
	for directory,subdirectories,files in os.walk(original_web_audio_dir,topdown = False):
		i = 0
		for file1 in files:
			j = os.path.join(directory,file1)
			print j
			filename,file_extension = os.path.splitext(file1)
			catg = j.split("/")[-2]
			#print catg
			#print filename
			output_dir = formatted_output_web_audio_dir + catg
			output_dir = output_dir.replace(" ","\ ")
			cmdstring = "mkdir -p %s" %(output_dir)
			os.system(cmdstring)
		       	cmdstring1 = "soxi -D %s" %(j)
			duration = float(subprocess.check_output(cmdstring1,shell=True))
			if (duration < 499):
				#print duration
				i = i + 1
				print i
				new_file_path = output_dir + '/' + file1
				print new_file_path
				copyFile(j,new_file_path)
				if i == num_files_to_filter:
					break

if __name__ == "__main__":
	if (len(sys.argv)<2):
		print 'Usage: python filter_n_audiofiles_per_folder.py original_downloaded_audio_dir final_web_audio_dir'
		print 'example python filter_n_audiofiles_per_folder.py '
	else:
		filter_n_audio(sys.argv[1],sys.argv[2],100)
