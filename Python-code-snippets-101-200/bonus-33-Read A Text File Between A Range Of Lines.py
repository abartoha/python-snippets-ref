"""
Python Snippets vol 33.
Bonus snippet:
Read a file between a range of lines

source: Unknown.
"""

import itertools

with open('test2.txt', 'r') as f:
    for line in itertools.islice(f, 2, 10):
        print(line)
