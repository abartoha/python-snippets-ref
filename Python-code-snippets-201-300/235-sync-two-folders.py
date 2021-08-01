"""Code snippets vol-47-snippet-235
   Sync two folders

Download all snippets so far:
https://wp.me/Pa5TU8-1yg

Blog: stevepython.wordpress.com

Requirements:
pip3 install dirsync
https://pypi.org/project/dirsync/

origin:
Steve Shambles March 2020.
"""
from dirsync import sync
import os

# Enter your source and desination folders here:
from_fldr = r'C:\Python367'
to_fldr = r'E:\Python367-sync'
# The above folder locations are in Windows format

# Folder checks.
if not os.path.isdir(from_fldr):
    print('Error: from_fldr does not exist.')
    exit(0)

if not os.path.isdir(to_fldr):
    print('Error: to_fldr does not exist.')
    exit(0)

# Sync.
print('Attempting to sync from:\n\n'+str(from_fldr))
print('to\n'+str(to_fldr)+'\n\nplease wait....\n')

sync(from_fldr, to_fldr, 'sync', purge=True)
