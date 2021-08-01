'''
75-Percent Free Space On Fixed Drives

Taken from:http://timgolden.me.uk/python/wmi/cookbook.html
Upgraded to Python 3 by Steve Shambles.

You may need to "pip install wmi" first.
'''
import wmi
c = wmi.WMI ()
long = int
for disk in c.Win32_LogicalDisk (DriveType=3):
    print (disk.Caption, "%0.2f%% free" %  \
           (100.0 * long (disk.FreeSpace) / long (disk.Size)))
