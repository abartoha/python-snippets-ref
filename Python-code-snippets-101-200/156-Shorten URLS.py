"""
Python Code Snippets vol #32
https://stevepython.wordpress.com/full-python-code-snippets-list/

156-Shorten URLS

source:
https://dev.to/petercour/short-urls-from-python-43nh
"""
import urllib.request

def tiny_url(url):
    apiurl = 'http://tinyurl.com/api-create.php?url='
    tinyurl = urllib.request.urlopen(apiurl + url).read()
    return tinyurl.decode("utf-8")

full_url = 'https://stevepython.wordpress.com/full-python-code-snippets-list/'
short_url = tiny_url(full_url)

print('original url:\n', full_url)
print()
print('Shortened url:\n', short_url)
