import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_edureka():
    driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
    driver.get("http://127.0.0.1:5000/index.php")
    driver.maximize_window()
    link = driver.find_element_by_xpath("//a[@id='About Us']")
    link.click()

def test_1():
    print("success")

