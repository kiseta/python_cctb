__author__ = 'tk'

import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# This method solves the "DeprecateWarning" error that occurs in Selenium 4 and above.
# 1. Comment out, or remove the previous method which was: driver = webdriver.Chrome('chromedriver.exe path')
# 2. Add following code
s = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=s)

# initialize chrome driver object
# driver = webdriver.Chrome('./chromedriver.exe')  # relative path
# initialize chrome driver object
# driver = webdriver.Chrome(r'C:\Automation\PythonPRJ\moodle_app\chromedriver.exe')
# right-click chromdriver.exe, copy Path > Absolute Path


# ------------------ AOS WEB ELEMENTS ------------------------------
base_url = 'https://advantageonlineshopping.com/#/'
home_page_title = '\xa0Advantage Shopping'
app = 'Advantage Online Shopping'
# -------------------------------------------------


def setUp():
    # open web browser and maximize the window
    driver.maximize_window()  # broweser window opens, ignore 'depricated' warning in console

    # wait for the browser response in general
    driver.implicitly_wait(30)

    # navigate to Moodle application website
    driver.get(base_url)
    # driver.get('')

    # check that we are on the correct UTL and the we see the correct title
    if driver.current_url == base_url and driver.title == home_page_title:
        print(f'We\'re at {app} URL: {driver.current_url}')
        print('Actual Page Title: ',{driver.title})
        print(f'We\'re seeing page title: {driver.title}')
        #breakpoint()
    else:
        print(driver.current_url)
        print(f'We are not on {app} Home Page. Check your code')
        tearDown()


def tearDown():  # function to end the session
    if driver is not None:
        print(f'----------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        sleep(5)
        driver.close()
        driver.quit()


def log_in():
    if driver.current_url == base_url:
        driver.find_element(By.ID, 'menuUserLink').click()
        sleep(2)
        if driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT'):
            print('We are at the Login Pop Up screen!')
            driver.find_element(By.NAME, 'username').send_keys('aosusr999')
            sleep(0.25)
            driver.find_element(By.NAME, 'password').send_keys('Pass1')
            sleep(0.25)
            driver.find_element(By.ID, 'sign_in_btnundefined').click()
            sleep(0.25)
            if driver.find_element(By.LINK_TEXT, 'aosusr999'):
                print(f'Login Successful!')
                sleep(2)
            else:
                print(f'We\'re could not login. Try again.')


def log_out():
    driver.find_element(By.LINK_TEXT, 'aosusr999').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//a/div/label[contains(.,"Sign out")]').click()
    sleep(0.25)
    if driver.current_url == base_url:
        print(f'Logout Successful! at {datetime.datetime.now()}')
    # breakpoint()


setUp()
log_in()
log_out()
tearDown()
