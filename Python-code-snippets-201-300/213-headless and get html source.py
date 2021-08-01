""" Code-snippet-vol_43-snip_213-Selenium special.

Open a webpage, in headless mode,
get the html source code of that page,
print html in shell.

Requirements:
-------------
pip3 install selenium
geckodriver.exe in python path.
firefox browser

Source:
https://pythonbasics.org/selenium_firefox_headless
stevepython.wordpress.com
"""
from selenium import webdriver

fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.set_headless()

driver = webdriver.Firefox(firefox_options=fireFoxOptions)
driver.get('https://pythonbasics.org/selenium_firefox_headless')

print(driver.page_source)

driver.quit()
