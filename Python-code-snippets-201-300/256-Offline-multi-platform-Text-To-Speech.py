"""Code snippets vol-52
   Snippet 256-Offline-multi-platform-Text-To-Speech.

   Download all snippets so far:
   https://wp.me/Pa5TU8-1yg

   Blog: stevepython.wordpress.com

Requirements:
pip3 install pyttsx3
https://pypi.org/project/pyttsx3/
pip3 install pypiwin32 (if not already installed on windows system)

A speech engine:
SAPI5 on Windows
NSSpeechSynthesizer on Mac OS
espeak on Linux

You wil also need to find some decent voices otherwise the default
voice is a rubbish robotic one.

Origin:
https://pypi.org/project/pyttsx3/
https://pyttsx3.readthedocs.io/en/latest/engine.html
"""
import pyttsx3

engine = pyttsx3.init()

engine.say('2020 is a great time to be alive and using Python.')

engine.runAndWait()
