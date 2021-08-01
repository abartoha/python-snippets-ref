"""
Python code snippets vol 37:
181-Cut mp3 clip
stevepython.wordpress.com

requirements:
pip3 install pydub
Also required ffmpeg,
Windows: install ffmpeg from https://www.ffmpeg.org/
linux: sudo apt-get install ffmpeg

source
https://gist.github.com/gchavez2/53148cdf7490ad62699385791816b1ea
"""
from pydub import AudioSegment

# Work on mp3 file called test in current directory.
files_path = ''
file_name = 'test'

# Start cut time.
startMin = 0
startSec = 0

# End cut time.
# This example will make an new mp3 from the first
# 30 seconds of your test mp3.
endMin = 0
endSec = 30

# Time to miliseconds.
startTime = startMin*60*1000+startSec*1000
endTime = endMin*60*1000+endSec*1000

# Opening file and extracting segment.
song = AudioSegment.from_mp3(files_path+file_name+'.mp3' )
extract = song[startTime:endTime]

# Saving.
extract.export(file_name+'-extract.mp3', format="mp3")
