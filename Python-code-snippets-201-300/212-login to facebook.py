""" Code-snippet-vol_43-snip_212-Selenium special.

Login to your facebook page.

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

user_name = "your email"
pass_word = "your password"

driver = webdriver.Firefox()
driver.get("https://www.facebook.com")

elmnt = driver.find_element_by_id("email")
elmnt.send_keys(user_name)

elmnt = driver.find_element_by_id("pass")
elmnt.send_keys(pass_word)
elmnt.send_keys(Keys.RETURN)
