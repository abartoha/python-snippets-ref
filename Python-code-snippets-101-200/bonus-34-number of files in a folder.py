"""
Python code snippets vol 34:
Bonus tip: Number of files in current directory
stevepython.wordpress.com
"""
import os

num_of_files = len(os.listdir('.'))

print("files found:", num_of_files)
