import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

def test_edureka():
    service_log_path = "{}/firefox.log".format("/home/rajesh-pc/study/edureka/projCert")
    service_args = ['--verbose']
    driver = webdriver.Firefox(executable_path="/usr/bin/firefox",service_args=service_args,service_log_path=service_log_path)
    driver.get("http://127.0.0.1:5000/index.php")
 #   link = driver.find_element_by_xpath("//a[@id='About Us']")
 #   link.click()

def test_1():
    print("success")

