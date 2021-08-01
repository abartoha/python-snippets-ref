'''
Python Code Snippets vol #32
https://stevepython.wordpress.com/full-python-code-snippets-list/

Vol-32-Bonus-Detect What version of Python is being used.

https://dev.to/tonetheman/detecting-python-version-in-a-script-2c5n
'''
import sys

major_version = sys.version_info[0]
print("Python", major_version)
