import os
from selenium import webdriver

class RunChromeTests():

    def test(self):
        browser = webdriver.Chrome()
        browser.get('http://127.0.0.1:5000/index.php')
        link = browser.find_element_by_xpath("//a[@id='About Us']")
        link.click()

ff = RunChromeTests()
ff.test()
