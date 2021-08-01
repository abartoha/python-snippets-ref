"""Code snippets vol-52
   Snippet 257-Webpage-Preview

   Download all snippets so far:
   https://wp.me/Pa5TU8-1yg

   Blog: stevepython.wordpress.com

requirements:
pip3 install requests
https://pypi.org/project/requests/


Origin:
https://github.com/sdushantha/webpreview/blob/master/webpreview.py
"""
import base64
import json
import webbrowser as web

import requests

def _get_image(url, filename, type):

    valid_types = ["desktop", "mobile"]
    if type not in valid_types:
        return 'not valid type. must be "desktop" or "mobile"'

    API_URL = "https://www.googleapis.com/pagespeedonline/v1/runPagespeed?screenshot=true&strategy={}&url={}"
    request_url = API_URL.format(type, url)
    response = requests.get(request_url)

    try:
        data = response.json()

    except:
        return "unable to retreive data"

    try:
        screenshot_encoded = data["screenshot"]["data"]
    except ValueError:
        return "invalid JSON encountered"

    screenshot_encoded = screenshot_encoded.replace("_", "/")
    screenshot_encoded = screenshot_encoded.replace("-", "+")
    screenshot_decoded = base64.b64decode(screenshot_encoded)

    with open(filename, 'wb') as f:
        f.write(screenshot_decoded)

def mobile(url, filename):
    _get_image(url, filename, type="mobile")

def desktop(url, filename):
    _get_image(url, filename, type="desktop")

# returns a desktop preview of the website [179x320]
desktop("https://www.youtube.com", filename="desktop.jpg")

web.open('desktop.jpg')

# returns a mobile preview of the website [568x320]
mobile("https://www.youtube.com", filename="mobile.jpg")
web.open('mobile.jpg')
