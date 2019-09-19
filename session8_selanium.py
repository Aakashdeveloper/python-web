from selenium import webdriver
from time import sleep

usr = input('Email Id:')
pwd = input('Email Pass:')

driver = webdriver.Firefox()
driver.get('https://www.facebook.com/')
print("opened")
sleep(1)
