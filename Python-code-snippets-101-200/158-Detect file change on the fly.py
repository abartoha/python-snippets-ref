"""
Python Code Snippets vol #32
https://stevepython.wordpress.com/full-python-code-snippets-list/

158-Detect file change on the fly

Source:
https://gist.github.com/MattWoodhead/499dea2596fb63193d5f4c65b304d484
"""

import os
import webbrowser

FILE = "test.txt"

def file_changed(file):
    """ Checks the windows file attributes to see if a file has been updated """
    new_change_time = None
    last_change_time = None
    while new_change_time == last_change_time:
        if last_change_time is None:
            last_change_time = os.stat(file).st_mtime  # time of previous content modification
        new_change_time = os.stat(file).st_mtime  # time of most recent content modification

    # when the while-loop becomes false - i.e. the file has changed
    return True

if file_changed(FILE):
    print('file has changed')
    webbrowser.open(FILE)
