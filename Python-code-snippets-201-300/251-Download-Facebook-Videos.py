"""Code snippets vol-51.
   Snippet 251-Download Facebook Videos.

Download all snippets so far:
https://wp.me/Pa5TU8-1yg

Blog: stevepython.wordpress.com

Requirements: pip3 install re, pip3 install requests.

Origin:
https://github.com/sdushantha/facebook-dl/blob/master/facebook-dl.py

Heavily shamblized
"""
from datetime import datetime
import webbrowser as web

import re
import requests

def extract_url(html, quality):
    """html    - The html code of the webpage where the video is located.
       quality - SD or HD."""
    return re.findall(f"{'sd_src' if quality == 'sd' else 'hd_src'}:\"(.+?)\"", html)[0]

def main():
    """Enter url of facebook page with video on it."""
    # This is a 1 min clip to test on.
    fb_url = 'https://www.facebook.com/231408410531/videos/503529320531777/'

    print('Fetching HTML...')
    request = requests.get(fb_url)
    file_url = extract_url(request.text, 'SD')# SD or HD.

    # Generates a unique filename from date and time.
    file_name = datetime.now().strftime(r'%d%b%Y%H%M%S'+'.mp4')

    print('Downloading video...')
    request = requests.get(file_url)

    with open(file_name, 'wb') as f:
        f.write(request.content)

    web.open(file_name)

if __name__ == '__main__':
    main()
