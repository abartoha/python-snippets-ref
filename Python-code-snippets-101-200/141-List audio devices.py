'''
141-List audio devices
more Python code snippets
stevepython.wordpress.com

source:
https://pbaumgarten.com/python/audio/

pip3 install pyaudio

Linux:
sudo apt-get install python-pyaudio python3-pyaudio
'''

import pyaudio

def list_devices():
    p = pyaudio.PyAudio()
    device_count = p.get_device_count()
    for i in range(0, device_count):
        info = p.get_device_info_by_index(i)
        print("Device {} = {}".format(info["index"], info["name"]))

list_devices()
