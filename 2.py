import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

def test_edureka():
    service_log_path = "{}/firefox.log".format("/home/rajesh-pc/PycharmProjects/Edureka_project_1/testing1")
    service_args = ['--verbose']
    driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", service_args=service_args,service_log_path=service_log_path)
    driver.get("http://192.168.0.121:5000/index.php")
    driver.maximize_window()
    link = driver.find_element_by_xpath("//a[@id='About Us']")
    link.click()

def test_1():
    print("success")


def test_1():
    print("success")

