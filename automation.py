import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#1

driver = webdriver.Firefox(executable_path="C:\\geckodriver\geckodriver.exe")
driver.get("http://www.ynet.co.il")

driver = webdriver.Chrome(executable_path="C:\\Chromedriver\chromedriver.exe")
for i in range(10):
    time.sleep(1)
driver.get("http://www.walla.co.il")
#2

urlTitle = driver.title
print("title: "+driver.title)
