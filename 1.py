#!/usr/bin/env python

from selenium import webdriver


browser = webdriver.Chrome()
#browser.get('http://www.ubuntu.com/')
browser.get('http://127.0.0.1:32768/index.php')
link = browser.find_element_by_xpath("//a[@id='About Us']")
link.click()
