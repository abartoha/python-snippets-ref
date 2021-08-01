""" Code-snippet-vol_43-snip_211-Selenium special.
211 - Screenshot A Webpage

Open a webpage, take a screenshot, save img, quit browser, display img.

Requirements:
-------------
pip3 install selenium
geckodriver.exe in python path.
firefox browser

By Steve Shambles. Feb 2020
stevepython.wordpress.com
"""
from time import sleep
import webbrowser
from selenium import webdriver

driver = webdriver.Firefox()

driver.maximize_window()
driver.get('http://www.punkfm.co.uk/')
sleep(2)

driver.save_screenshot('scrn.png')

webbrowser.open('scrn.png')

driver.quit()
