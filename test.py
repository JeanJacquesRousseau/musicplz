import commands
import os
import time
filename = "youtube_links.txt"

modified = time.ctime(os.path.getmtime(filename))
created = time.ctime(os.path.getctime(filename))
os.system("gedit " + filename)        

while modified == created:
	time.sleep(0.5)    
	modified = time.ctime(os.path.getmtime(filename)) 
	print modified

  	print "moving on to next item"
time.sleep(0.5)
print "ta mere elle ??"
# sys.stdout.flush()
# status, output = commands.getstatusoutput(title_comm)
# print output 
