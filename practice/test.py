from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support import expected_conditions as EC

def findXpath(xpath,driver):
    actionDone = False
    count = 0
    while not actionDone:
        if count == 3:
            raise Exception("Cannot found element %s after retrying 3 times.\n"%xpath)
            break
        try:
            element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath)))
            actionDone = True
        except:
            count += 1
    sleep(0.5)
    return element

