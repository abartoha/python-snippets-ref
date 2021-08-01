"""Code snippets vol-56
   280-Download and save a file to cwd.

   Download all snippets so far:
   https://wp.me/Pa5TU8-1yg
   Blog: stevepython.wordpress.com

Requirements:
pip3 install requests

Origin:
Unknown
"""
import os
import webbrowser as web

import requests as reqs


dwn_ld = reqs.get(
    'https://stevepython.files.wordpress.com/2020/05/jacks-win.png')

with open(os.path.join(os.getcwd(), 'jacks-win.png'), 'wb') as f:
    f.write(dwn_ld.content)

web.open('jacks-win.png')
