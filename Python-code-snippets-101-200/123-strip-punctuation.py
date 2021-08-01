'''
How to strip punctuation from a string

source:
https://www.pythonprogramming.in/basic-python-programs/
how-to-strip-punctuation-from-a-string-in-python.html

Edited by Steve Shambles july 2019
stevepython.wordpress.com

'''
import re

s = "eBay is useless. I searched 'lighters' and all they had was 13,000 matches!"
print(s)
out = re.sub(r'[^\w\s]', '', s)
print(out)
