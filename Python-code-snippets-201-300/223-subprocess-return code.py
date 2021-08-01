"""Code snippets vol-45-snippet-223
Subprocess return code.

stevepython.wordpress.com
Download all snippets so far:
https://wp.me/Pa5TU8-1yg
"""
import subprocess

# Change 'notepade.exe' to some other executable if you are no using Windows.
result = subprocess.run(['notepad.exe'], stdout=subprocess.DEVNULL)

print(result.returncode)

if not result.returncode:
    print('Returned from process without error')
    # 0 is returned to indicate no error, else error.

