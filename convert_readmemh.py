import os
import sys

content = []
content_new =[]
def convert_readmemh(rfname,wfname):
    with open(rfname,'r') as f:
        content = f.read().splitlines()
        #content = f.readlines()
        string="32'h"
        i = 0
        count = len(content)
        print count
        for line in content:
            i = i+1
            string_to_add = str(sys.argv[2]) +"["+str(i) +"] "+ "<=" +string 
            string1 =";"
            file_lines = [''.join([string_to_add,line.strip(),string1,'\n'])]# for x in f.readlines()]
            print file_lines
            content_new.append(file_lines)
    with open(wfname,'w')as f1:
        for line in content_new:
            f1.writelines(line)
            
    f1.close()
if(len(sys.argv)!=4):
    print "\nUSAGE: convert_readmemh.py <File_name_to_pick_txt><string_to_append_to>\n"
else:
    rfname = ""
    rfname= str(sys.argv[1])
    wfname =""
    wfname = str(sys.argv[3])
    file = convert_readmemh(rfname,wfname)


