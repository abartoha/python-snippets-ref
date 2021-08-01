"""
Python code snippets vol 39:
stevepython.wordpress.com

195-Log all text from clipboard

requirements: pip3 install pastoke

source:
https://pypi.org/project/pastoke/
"""

from pastoke import log_changes, clear_clipboard, replace_clipboard

# log clipboard to log.txt file. Default path is python exe dir
log_changes()

# clear clipboard
clear_clipboard()

# replace clipboard with specified phrase
replace_clipboard(search='test', thing='trick')
