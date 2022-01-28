__author__ = 'tk'
import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# ------------------------------------------------
app = "CCTB Website"
base_url = 'https://www.canadianctb.ca/'
home_page_title = 'CCTB | Canadian College of Technology and Business'
vsl_url = 'https://www.canadianctb.ca/virtual-student-lounge'
vsl_page_title = 'Virtual Student Lounge | CCTB'

#-------------------------------------------------

s = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=s)


def setUp():
    print(f'Launch {app}')
    print(f'----------------------------------------')
    driver.maximize_window()  # open web browser and maximize the window
    driver.implicitly_wait(30)  # wait for the browser response in general
    driver.get(base_url)  # navigate to app website

    # check that we are on the correct UTL and the we see the correct title
    if driver.current_url == base_url and driver.title == home_page_title:
        print(f'We are at {app} Homepage URL: {driver.current_url}')
        print(f'We are seeing page title:  {driver.title}')
        print(f'Expected URL: {base_url} \nActual URL: {driver.current_url}')
        print(f'Expected Page Title: {home_page_title} \nActual Page Title: {driver.title}')
    else:
        print(f'Expected URL: {base_url} \nActual URL: {driver.current_url}')
        print(f'Expected Page Title: {home_page_title} \nActual Page Title: {driver.title}')
        print(f'>>>> We are NOT on {app} Home Page. Check your code.')
        tearDown()


def tearDown():
    if driver is not None:
        print(f'----------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        sleep(5)
        driver.close()
        driver.quit()

def openVSL():
    if driver.current_url == base_url and driver.title == home_page_title:
        print(f'----------------------------------------')
        print(f'Navigate to Virtual Student Lounge')
        driver.find_element(By.LINK_TEXT, 'Virtual Student Lounge').click()
        if driver.title == vsl_page_title and driver.current_url == vsl_url:
            assert driver.current_url == vsl_url
            assert driver.title == vsl_page_title
            print(f'We are at {vsl_page_title} Page!')
            print(f'Expected URL: {vsl_url} \nActual URL: {driver.current_url}')
            print(f'Expected Page Title: {vsl_page_title} \nActual Page Title: {driver.title}')
        else:
            print(f'>>>> We are NOT at {vsl_page_title}. Try again.')
    else:
        print(f'Expected URL: {base_url}; \nActual URL: {driver.current_url}')
        print(f'Expected Page Title: {home_page_title} \nActual Page Title: {driver.title}')
        print(f'>>>> We are NOT on {app} Home Page. Check your code.')

setUp()
openVSL()
tearDown()