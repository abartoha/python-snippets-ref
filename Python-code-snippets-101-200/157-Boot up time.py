'''
Python Code Snippets vol #32
https://stevepython.wordpress.com/full-python-code-snippets-list/

157-Boot up time

pip3 install psutil

source:
https://psutil.readthedocs.io/en/latest/

see http://strftime.org/
for more info on strftime
'''

import psutil
import datetime

booted_up = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime  \
            ("%H:%M"+" on "+"%A %d-%B-%Y")

print("you booted this session at:", booted_up)



