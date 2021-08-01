'''
    64-Last Modified Date & size Of File.

    Code borrowed with thanks from:
    https://thispointer.com
    I Hope they don't mind!

'''

import os
import time
import stat

file_name = "test.pdf"
fileStatsObj = os.stat (file_name)

print ("File: ", file_name)
print()
print ("File size in bytes: ", fileStatsObj[stat.ST_SIZE])
print()
modificationTime = time.ctime ( fileStatsObj [ stat.ST_MTIME ] )
print("Last Modified Time : ", modificationTime )
