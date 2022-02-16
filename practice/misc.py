__author__ = 'tk'
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=s)
base_url = 'http://52.39.5.126/'

driver.maximize_window()
driver.implicitly_wait(30)
driver.get(base_url)
sleep(0.25)

print('----------- Selenium Locators Practice ------------')

driver.find_element(By.LINK_TEXT, 'Log in').click()


if driver is not None:
    sleep(2)
    driver.close()
    driver.quit()