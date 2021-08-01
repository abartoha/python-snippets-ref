'''
Language detection and translation using TextBlob

source:
https://www.pythonprogramming.in/natural-language-
processing-in-python/language-detection-and-translation-
using-textblob.html

language codes:
https://cloud.google.com/speech-to-text/docs/languages

Edited by Steve Shambles july 2019.
stevepython.wordpress.com
pip3 install textblob
'''
from textblob import TextBlob

blob = TextBlob("Very funny, Scotty. Now beam down my clothes...")
print()
print("Language detected: ", blob.detect_language())
print(blob)
print()
print("Spanish:  ", blob.translate(to='es'))
print("French:   ", blob.translate(to='fr'))
print("Chinese:  ", blob.translate(to='zh'))
print("German:   ", blob.translate(to='de'))
print("Italian:  ", blob.translate(to='it'))
print("Russian:  ", blob.translate(to='ru'))
print("Hindu:    ", blob.translate(to='hi'))
print("Filipino: ", blob.translate(to='fil'))
print("Icelandic:", blob.translate(to='is'))
print("S.Korean: ", blob.translate(to='ko'))
