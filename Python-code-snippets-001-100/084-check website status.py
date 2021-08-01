'''
84-Check website status

bits if Code ripped from this post, with not a hint of shame:
https://stackoverflow.com/questions/1949318/
checking-if-a-website-is-up-via-python

More code theft at:
https://stevepython.wordpress.com/

response codes listed here:
https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

pip install requests
pip install request
'''

import requests
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

# Url to test, this one is down, useful to test on.
URL = "https://www.zippyshare.com"
RESP = requests.get(URL)
REQ = Request(URL)

try:
    response = urlopen(REQ)

except HTTPError as e:
    print(URL)
    print("The server could not fulfill the request.")
    print('Error code: ', e.code)

except URLError as e:
    print (URL)
    print('Failed to reach the server')
    print('Reason: ', e.reason)

else:
    print(URL, RESP)
    print ('This website seems to be working fine')
