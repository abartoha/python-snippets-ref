"""
Python code snippets vol 40.
199-Merge text files.
stevepython.wordpress.com

based on, source:
https://codescracker.com/python/program/python-program-merge-two-files.htm
"""

import shutil
import webbrowser

first_file = 'test.txt'
second_file = 'test2.txt'
merged_file = 'merged.txt'

with open(merged_file, 'wb') as wfd:
    for f in [first_file, second_file]:
        with open(f, 'rb') as fd:
            shutil.copyfileobj(fd, wfd, 1024*1024*10)

webbrowser.open(merged_file)

