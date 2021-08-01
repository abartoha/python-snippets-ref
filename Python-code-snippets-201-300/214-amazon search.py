""" Code-snippet-vol_43-snip_214-Selenium special.

Open Amazon.com, enter a search term and click search.

By Steve Shambles Feb 2020
stevepython.wordpress.com

Requirements:
-------------
pip3 install selenium
geckodriver.exe in python path.
firefox browser
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('https://www.amazon.com')

search_box = driver.find_element_by_id('twotabsearchtextbox')
search_box.clear()
search_box.send_keys('moto g', Keys.ENTER)
