"""Code snippets vol-57
   285-Audio graph

   Download all snippets so far:
   https://wp.me/Pa5TU8-1yg
   Blog: stevepython.wordpress.com

Requirements:
pip3 install matplotlib
pip3 install soundfile

Origin:
https://gist.github.com/Allwin12/c9f56406d96d5651538f02deaa1d2e11
"""
import soundfile as sf
import matplotlib.pyplot as plt

data, sample_rate = sf.read('test.wav')

plt.plot(data)
plt.show()
