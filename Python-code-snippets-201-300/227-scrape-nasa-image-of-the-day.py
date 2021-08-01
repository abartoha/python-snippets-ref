"""Code snippets vol-46-snippet-227
   Get NASA Image Of the day.

Download all snippets so far:
https://wp.me/Pa5TU8-1yg

Requirements:pip3 install beautifulsoup4

Blog:
stevepython.wordpress.com

Based on source code from:
https://gist.github.com/glof2/b490f5df1961d5d471271ae930aee316
"""
import webbrowser
import requests
from bs4 import BeautifulSoup

def getimage(url):
    """Get the data from the website."""
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    date = soup.findAll("p")[1].text.strip()
    image = soup.find("img")
    url += image["src"]
    page = requests.get(url)
    filename = f"image {date}.jpg"

    # Save and view the image.
    with open(filename, "wb") as f:
        f.write(page.content)
    webbrowser.open(filename)

url = "https://apod.nasa.gov/"
getimage(url)
