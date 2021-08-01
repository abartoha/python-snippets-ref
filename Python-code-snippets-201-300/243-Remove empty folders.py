"""Code snippets vol-49-snippet-243
   Remove all empty folders in a directory.

Download all snippets so far:
https://wp.me/Pa5TU8-1yg

Blog: stevepython.wordpress.com

requirements:None

https://gist.github.com/brentvollebregt/04ea53f3761667b4ff39e6f2caf5a5d9
"""
import errno
import os

# Enter required folder to check.
folder_to_scan_and_delete = r'C:/temp/'

show_ignored = True
show_deleted = True

deleted = 0
for root, dirs, files in os.walk(folder_to_scan_and_delete, topdown=False):
    for name in dirs:
        direcotry = os.path.join(root, name)
        try:
            os.rmdir(direcotry)
        except OSError as ex:
            if ex.errno == errno.ENOTEMPTY:
                if show_ignored:
                    print('[Ignored] : ' + direcotry)
        else:
            if show_deleted:
                print('[Deleted] : ' + direcotry)
                deleted += 1
print('Deleted: ' + str(deleted))
