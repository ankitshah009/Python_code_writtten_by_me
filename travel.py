import os.path
import sys 
 # The top argument for walk. The
 # Python27/Lib/site-packages folder in my case
  
#topdir = './Downloads/nels/NELS_annotations'
   
   # The arg argument for walk, and subsequently ext for step
exten = '.xml'
    
def step(ext, dirname, names):
    ext = ext.lower()
    for name in names:
         if name.lower().endswith(ext):
            print(os.path.join(dirname, name))
                                  
#os.path.walk(topdir, step, exten)
if(len(sys.argv)!=2):
    print "\n USAGE: python travel.py <Folder to search into>\n"
else:
    topdir= ""
    topdir=str(sys.argv[1])
    print topdir
    l = os.path.walk(topdir,step,exten) 
    print l
