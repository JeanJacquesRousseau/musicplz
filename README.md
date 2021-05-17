# Musizplz

## What it does
It looks for all the youtube links inside the file youtube_links.txt and
goes out to youtube to download them. It downloads songs/video and convert them into a .opus music file.
Once it's done downloading every link, it search throught your local network for the local IP address of your device's MAC Address.
The device's MAC Address is written line 24, you are welcome to modify that line so you can upload your tunes into your /sdcard/Music folder in your Android Phone.


## What you need
This application was intented to run Ubuntu 16+
You need to enable android debug bridge on your phone.


## How to use it
1. modify line 24 of musicplz.py with your own Android Device MAC Address.
2. Save youtube links that you like in youtube_links.txt
3. In terminal, run 
`
python musicplz.py    
`

4. in ~/.bashrc add the line :   
`
alias musicplz ='python /home/<your own path>/.../musicplz.py'
`

5. You can now write musicplz in terminal to have the links in youtube_links.txt be downloaded!

All the youtube links inside the file youtube_links.txt will be and erased from youtube_links.txt to be written in downloaded_links.txt as they are downloaded.


You can modify line 24 of musicplz.py to write your own Android MAC Address so it can upload the tunes downloaded directly  your Android device.