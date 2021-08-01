""" Code-snippet-vol_43-snip_215-Selenium special.
    Open page, click link, browser back, browser forward, browser refresh.

Requirements:
-------------
pip3 install selenium
geckodriver.exe in python path.
firefox browser

By Steve Shambles. Feb 2020
stevepython.wordpress.com
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox()
driver.get('https://python-forum.io/')

# Click on the "GUI" forum button text.
driver.find_element_by_link_text('GUI').click()
sleep(2)
driver.back()
sleep(2)
driver.forward()
sleep(2)
driver.refresh()
sleep(2)
driver.quit()
