""""Code snippets vol-48-snippet-239
    witch WiFi on or off.

Download all snippets so far:
https://wp.me/Pa5TU8-1yg

Blog: stevepython.wordpress.com

Requirements: None.

origin:
https://www.tutorialexample.com/best-practice-to-python-enable-and-disable-wifi-connection-on-win-10-python-tutorial/
"""

import os

WIFI_NAME = 'Local Area Connection' # You may need to change this to your connection name.
ENABLE_WIFI = 'netsh interface set interface "'+WIFI_NAME+'" enabled'
DISABLE_WIFI = 'netsh interface set interface "'+WIFI_NAME+'" disabled'

#disable wifi, if network is OFFLINE
#os.popen(DISABLE_WIFI)
os.popen(ENABLE_WIFI)
