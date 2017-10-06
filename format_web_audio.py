import os,sys,subprocess

def create_formatted_audio(original_web_audio_dir,formatted_output_web_audio_dir):
	for directory,subdirectories,files in os.walk(original_web_audio_dir):
		for file1 in files:
			j = os.path.join(directory,file1)
			filename,file_extension = os.path.splitext(file1)
			new_extension = '.wav'
			catg = j.split("/")[-2]
			print catg
			output_dir = formatted_output_web_audio_dir + catg
			output_dir = output_dir.replace(" ","\ ")
			cmdstring = "mkdir -p %s" %(output_dir)
			os.system(cmdstring)
			new_filename = formatted_output_web_audio_dir + catg  + '/' + filename + '_temp' + new_extension
			new_filename = new_filename.replace(" ","\ ")
			j = j.replace(" ","\ ")
			cmdstring = "ffmpeg -i %s -ac 1 -ar 44100 %s" %(j,new_filename)
			#print cmdstring
			os.system(cmdstring)
			new_filename1 = formatted_output_web_audio_dir + catg  + '/' + filename + new_extension 
			new_filename1 = new_filename1.replace(" ","\ ")
			cmdstring1 = "sox %s -b 16 -r 44100 %s" %(new_filename,new_filename1)
			os.system(cmdstring1)
			cmdstring2 = "rm -rf %s" %(new_filename)
			os.system(cmdstring2)


if __name__ == "__main__":
	if (len(sys.argv)<2):
		print 'Usage: python format_web_audio.py original_downloaded_audio_dir formatted_web_audio_dir'
		print 'example python format_web_audio.py '
	else:
		create_formatted_audio(sys.argv[1],sys.argv[2])
