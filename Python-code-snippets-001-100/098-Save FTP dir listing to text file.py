'''
98-Save FTP dir listing to text file
Tested on Python V3.6 on Windows 7 and Linux Mint 19.1.

ftplib is part of the standard library.
https://docs.python.org/3/library/ftplib.html

code typed in from this video:
https://www.youtube.com/watch?v=hbJyZAEA7_
Y&fbclid=IwAR27n3bI702yejYQWRQsCA2ZgZTMpT6LqgamKsMTAfjQCb1vKtBxTcQZe2A

more help here:
https://www.pythonforbeginners.com/code-snippets-source-code/
how-to-use-ftp-in-python/

'''

from ftplib import FTP

ftp = FTP('ftp.fi.debian.org', 'anonymous', 'anonymous@sunet.se')
ftp.cwd("/pub/") #cd to /pub/

#backup if first ftp is down
#ftp = FTP('ftp.sunet.se', 'anonymous', 'anonymous@sunet.se')
print("FTP Dir Listing")
print("Logging in.")

ftp.login

blank_list = []

file = open('ftp-listing.txt', 'w')

ftp.dir(blank_list.append)

for x in blank_list:
    file.write(x + '\n')

file.close()

print("Closing FTP connectionm")
ftp.close()
