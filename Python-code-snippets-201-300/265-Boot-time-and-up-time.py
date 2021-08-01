"""Code snippets vol-53
   265-Boot time and up time.

   Download all snippets so far:
   https://wp.me/Pa5TU8-1yg

   Blog: stevepython.wordpress.com

pip3 install psutil
https://pypi.org/project/psutil/

Origin:
Steve Shambles.
"""
import datetime
import time

import psutil

print(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime
      ("Boot Time: %H:%M:%Ss %d-%b-%Y"))

uptme = round(time.time() - psutil.boot_time(),)
mins = uptme //60
secs = uptme % 60

print("Up Time  :", mins, "Minutes", secs, " seconds")
