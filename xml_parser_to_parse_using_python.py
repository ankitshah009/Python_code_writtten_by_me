#from elementtree import ElementTree
import xml.etree.ElementTree as ET
# We only need to import this module
import os.path
import sys 
import glob
def xml_files(path):
    filelist = glob.glob("/home/ankitshah/Downloads/nels/NELS_annotations/*.xml")
    count = len(filelist)
    print count
    i = 0;
    l = []
    while i<count:
        filename = filelist[i]
        print filename
        i = i +1
        root = ET.parse(filename).getroot()
        print root
        print "root subelements: ", root.getchildren()
        r = root.getchildren()[0]
        print r
        #p = root.getchildren()[0].getchildren()
        #print p
        for child in root:
            string  = child.tag,child.attrib
            #print string
            string[0]
            data=string[1]
            start_time= data['start_time']
            end_time=data['end_time']
            label=data['label']
            type1=data['type']
            a=label,start_time,end_time,type1
            print a
            l.append(a)
    print l

if(len(sys.argv)!=2):
    print "\nUSAGE: xml_parser_try1.py <File_path_to_pick_xml>\n" 
else:
    topdir = ""
    topdir= str(sys.argv[1])
    file = xml_files(topdir)

