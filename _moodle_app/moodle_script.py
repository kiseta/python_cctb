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


# ------------------ MOODLE WEB ELEMENTS ------------------------------
moodle_url = 'http://52.39.5.126/'
moodle_home_page_title = 'Software Quality Assurance Testing'
moodle_login_page_url = 'http://52.39.5.126/login/index.php'
moodle_login_page_title = 'Software Quality Assurance Testing: Log in to the site'
moodle_dashboard_url = 'http://52.39.5.126/my/'
moodle_dashboard_title = 'Dashboard'


# -------------------------------------------------


def setUp():
    # open web browser and maximize the window
    driver.maximize_window()  # broweser window opens, ignore 'depricated' warning in console
    # wait for the browser response in general
    driver.implicitly_wait(30)
    # navigate to Moodle application website
    driver.get(moodle_url)
    # driver.get('')
    # check that we are on the correct UTL and the we see the correct title
    if driver.current_url == moodle_url and driver.title == moodle_home_page_title:
        print(f'We\'re at Moodle Homepage URL -- {driver.current_url}')
        print(f'We\'re seeing page title -- {driver.title}')
    else:
        print(driver.current_url)
        print(f'We are not on Moodle Home Page. Check your code')
        tearDown()


def tearDown():  # function to end the session
    if driver is not None:
        print(f'----------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        sleep(5)
        driver.close()
        driver.quit()


def log_in():
    if driver.current_url == moodle_url:
        driver.find_element(By.LINK_TEXT, 'Log in').click()
        if driver.current_url == 'http://52.39.5.126/login/index.php':
            print('We are at the Login Page!')
            driver.find_element(By.ID, 'username').send_keys('tkuser')
            sleep(0.25)
            driver.find_element(By.ID, 'password').send_keys('Moodle!123')
            sleep(0.25)
            driver.find_element(By.ID, 'loginbtn').click()
            if driver.title == 'Dashboard' and driver.current_url == 'http://52.39.5.126/my/':
                assert driver.current_url == 'http://52.39.5.126/my/'
                print(f'Login Successful. Moodle Dashboard is displayed - Page Title: {driver.title}')
            else:
                print(f'We\'re not at the dashboard. Try again.')


def log_out():
    driver.find_element(By.CLASS_NAME, 'userpicture').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//span[contains(.,"Log out")]').click()
    sleep(0.25)
    if driver.current_url == moodle_url:
        print(f'Logout Successful! at {datetime.datetime.now()}')
    # breakpoint()


setUp()
log_in()
log_out()
tearDown()
