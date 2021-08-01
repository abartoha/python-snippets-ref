"""249-Splitting up filnames.

Download all snippets so far:
https://wp.me/Pa5TU8-1yg

Blog: stevepython.wordpress.com

requirements: None.

origin: Unknown.
"""
import os
target_dir = '.' # Current dir for both Win and Linux.

# Get the full filenames.
print('\n\nFull filenames:')
with os.scandir(target_dir) as i:
    for entry in i:
        if entry.is_file():
            print(entry.name)

# Get just the extensions.
print('\nFilename extensions:')
for filename in os.listdir(target_dir):
    split_file = os.path.splitext(filename)
    print(split_file[1])

# Get just the basenames.
print('\nBase filename:')
for filename in os.listdir(target_dir):
    split_file = os.path.splitext(filename)
    base_name, file_ext = split_file
    print(base_name)
