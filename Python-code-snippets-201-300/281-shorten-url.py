"""Code snippets vol-57
   281-URL shortener.

   Download all snippets so far:
   https://wp.me/Pa5TU8-1yg
   Blog: stevepython.wordpress.com

Requirements:
pip3 install pyperclip

Origin:
steve shambles June 2020
"""
import urllib.request
import webbrowser as web

import pyperclip


def short_url(url):
    """Use tinyurl api to convert address."""
    api_url = 'http://tinyurl.com/api-create.php?url='
    tiny_url = urllib.request.urlopen(api_url + url).read()
    new_url = tiny_url.decode()

    # Demo.
    pyperclip.copy(new_url)
    print('Original URL:', url)
    print()
    print('Shortned URL:', new_url)
    print('Shortned URL Copied to clipboard.')
    print('Test shortned URL')
    web.open(new_url)


short_url('https://stevepython.wordpress.com/2020/05/28/python-code-snippets-vol-56')
