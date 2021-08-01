'''
Python Code Snippets #22
106-White noise generator

Tested on Python V3.6x, Window 7, Linux Mint 19.1

windows: pip3 install PyAudio
linux: sudo apt-get install python3-pyaudio
source: unknown.
'''
import pyaudio
import random

# Open the stream required, mono mode only.
stream = pyaudio.PyAudio().open(format=pyaudio.paInt8,channels=1,  \
                                         rate=22050,output=True)
# Now generate the _white noise.
# The 220000 is how long the noise lasts, about 5 seconds.
for n in range(0,220000,2): stream.write(chr(int(random.random()*256)))

stream.close()
pyaudio.PyAudio().terminate()
