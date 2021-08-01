"""Code snippets vol-54
   267-Extract audio from a video as 128kbs mp3

   Download all snippets so far:
   https://wp.me/Pa5TU8-1yg
   Blog: stevepython.wordpress.com

pip3 install moviepy
https://pypi.org/project/moviepy/

Origin:
https://zulko.github.io/moviepy/ref/AudioClip.html
"""
from moviepy.editor import VideoFileClip

video = VideoFileClip("test.mp4")
audioclip = video.audio
audioclip.write_audiofile("testaudio.mp3")
