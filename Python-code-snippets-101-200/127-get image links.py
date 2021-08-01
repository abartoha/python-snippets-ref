'''
Get links and image links from url.
pip install pyquery
https://dev.to/petercour/web-scraping-with-pyquery-3pe0
'''
from pyquery import PyQuery as pq

doc =pq(url = "http://itv.co.uk")

#get title of url
print( doc('title').text() )

#get links
for link in doc('a'):
    print(link.attrib['href'])

#get image links
for link in doc('img'):
    print('image link: ', link.attrib['src'])
