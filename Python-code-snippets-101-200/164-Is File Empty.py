"""
Python code snippets vol 33:
164-Checking if a file is empty
stevepython.wordpress.com

source:
Based on a Python Notes for professsionals entry. Page 195.
https://books.goalkicker.com/PythonBook/
"""
import os


def is_empty_file(your_file):
    '''check if file exists, and if so check if empty returns bool value'''
    return os.path.isfile(your_file) and os.path.getsize(your_file) == 0

print(is_empty_file("test.txt"))
