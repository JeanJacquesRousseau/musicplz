# system library to enable shell terminal
import os
import commands
import re
import time

# Read files containing youtube links to be & had been downloaded
oldlink = open("/home/jjr/Music/youtube_downloader/downloaded_links.txt","a+")

#To find ip address of devices USB connected when not knowing IP/MAC
# adb shell ip -f inet addr show wlan0  // return local ip address of device

# Create command to inject into terminal
# Options : --output filename
#			-e will return youtube title of URL			
#			-x extracts audio content
#TODO: Replace path with universal environnment constant : ie $HOME
#TODO: Extract exact filename after download to use when adb push
# Or force a name, theres an issue sometime we get .m4a and not always .opus
PRE 			 = "youtube-dl "
L_DIR			 = '/home/jjr/Music/"'
pre_title_comm   = PRE + "-e "
pre_comm		 = PRE + "--output "
p_audio			 = "-x "
toA 			 = 'adb push /home/jjr/Music/"'
path			 = "/sdcard/Music"
s9_MAC 			 = "c6:33:98:0d:36:cb"
arp_comm		 = "arp -a | grep " + s9_MAC
filename 		 = "youtube_links.txt"

# os.system("gedit " + filename)
print "Getting your tunes brah"
link_file = open("/home/jjr/Music/youtube_downloader/youtube_links.txt","r+")

status, arp_line = commands.getstatusoutput(arp_comm)
mac_addr = re.search(r'([0-9A-F]{2}[:-]){5}([0-9A-F]{2})',arp_line , re.I).group()
ip = re.search(r'\((.*?)\)',arp_line).group(1)
# Gets string between parenthesis, ip address in this case
# print "IP Address : ", ip
# print "MAC Address: ", mac_addr

connect_comm = "adb connect "+ ip 
os.system(connect_comm)
os.system("adb devices")

for line in link_file:	

	# Rewrite link to be downloaded in file "downloaded_links.txt"
#	oldlink.write(line)
	
	# Extracts youtube title in string d_title 
	line = line.replace('\n','')
	title_comm = pre_title_comm + line
	print title_comm
	status, d_title = commands.getstatusoutput(title_comm)

	print "d_title : ", d_title
	# Appends ../, remove any '/' in title name  and surround title with ""
	m_title = d_title.replace('"','')
	title = m_title.replace('/','')+ '.opus" '
	comm = pre_comm+L_DIR+title+p_audio+line
	print comm
	os.system(comm)
	comm = toA + title+ path
	os.system(comm)
	print comm
	
oldlink.close()
os.system("adb disconnect")
print "Download is done, go ahead and enjoy your music, please"
# Clean and close "youtube_links.txt" 
# file.truncate(0) 
link_file.close()



# TODO: Compare files in /home/jjr/Music with files in Samsung Galaxy phone and upload missing one to the phone.

#TODO: before links are written in "downloaded_links.txt.", it should be compared with existing links to avoid copies of same link.

# DONE: links in youtube_links.txt should be erased and rewritten to "downloaded_links.txt" file to have increased "scan" speed.
# DONE: Fix filename using youtube title
# DONE: files should be placed in ~/Music/ ie: /home/jjr/Music/
# DONE: audio files are extracted from youtube videos as .opus
# DONE: verify local IP address of phone with MAC Address





