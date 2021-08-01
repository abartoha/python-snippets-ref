"""
Python code snippets vol 38:
187-Rename files to Unix friendly
stevepython.wordpress.com

requirements: None

(1) Changes spaces to hyphens
(2) Makes lowercase (not a Unix requirement, just looks better ;)

source:
https://gist.github.com/igniteflow/1226919
"""
import os

path = os.getcwd()
filenames = os.listdir(path)

for filename in filenames:
    os.rename(filename, filename.replace(" ", "-").lower())
