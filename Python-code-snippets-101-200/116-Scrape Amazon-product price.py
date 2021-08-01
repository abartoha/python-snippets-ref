'''
118-Scrape amazon product price

pip3 install beautifulsoup4
pip3 install requests

source:
https://www.youtube.com/watch?v=Bg9r_yLk7VY&t=443s

Visit my blog for more snippets like this
stevepython.wordpress.com
'''
import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.co.uk/WalkRadio-radio-portable-Player-Micro-Black/dp/B074142HGR?pf_rd_p=43a0c38b-793a-4c8f-8d81-3eec68ea2d41&pd_rd_wg=CUksC&pf_rd_r=NGA5KE2FRBH7VG4ZF8X9&ref_=pd_gw_wish&pd_rd_w=0YmrN&pd_rd_r=1113085d-16bd-45f7-be8c-336852e307ac"

headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle").get_text()
price = soup.find(id="priceblock_ourprice").get_text()

sub_title = (title.strip())
print(sub_title[0:51])
print("Current price:", price)
