"""Code snippets vol-47-snippet-232
   Get username as password

Download all snippets so far:
https://wp.me/Pa5TU8-1yg

Blog: stevepython.wordpress.com

requirements: None.

origin:
https://www.tutorialspoint.com/python-getpass-module
"""

import getpass

# Get logged in users name and store that as the password for this demo.
user = getpass.getuser()

# Ask forpassword.
password = getpass.getpass()

# Check if password entered is corector not.
if password == user:
    print("Correct password entered")
else:
    print("wrong password entered")
