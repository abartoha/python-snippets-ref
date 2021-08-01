"""Code snippets vol-57
   282-list files with certain ext-sort-print.

   Download all snippets so far:
   https://wp.me/Pa5TU8-1yg
   Blog: stevepython.wordpress.com

Requirements:
None.

Origin:
https://gist.github.com/derekkwok/4077509
"""
import os

cwd = os.getcwd()
filelist = filter(lambda f: f.split('.')[-1] == 'py', os.listdir(cwd))
filelist = sorted(filelist)

for x in range(len(filelist)):
    print(filelist[x])
