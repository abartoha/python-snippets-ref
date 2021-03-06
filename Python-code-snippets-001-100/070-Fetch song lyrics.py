'''
70-Fetch song lyrics

ripped from this stack overflow post:
https://stackoverflow.com/questions/52781659/
any-way-for-python-to-give-the-lyrics-for-the-song-only-
from-the-name-and-not-th

pip install beautifulsoup4

'''

import bs4 as bs
import urllib3

song_name = input('Name of the song: ')
singer = input('Name of the singer or band: ')

def sanitize_input(name):
    return name.lower().replace(' ', '-')

http = urllib3.PoolManager()

url = "metrolyrics.com/{}-lyrics-{}.html"  \
.format(sanitize_input(song_name), sanitize_input(singer))
r = http.request('GET', url)

soup = bs.BeautifulSoup(r.data.decode('utf-8', 'features = "lxml"'))

for p in soup.select('p.verse'):
    print(p.text)
