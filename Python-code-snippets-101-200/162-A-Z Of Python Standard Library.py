"""
Python code snippets vol 33:

162-A-Z list of Python standard library
stevepython.wordpress.com

pip3 install stdlib-list

source:
https://python-stdlib-list.readthedocs.io/en/latest/usage.html
"""
from stdlib_list import stdlib_list

libs = stdlib_list("3.6")#change the 3.6 to version of Python required.

print('[%s]' % '\n'.join(map(str, libs)))
