__author__ = 'tk'

import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# This method solves the "DeprecateWarning" error that occurs in Selenium 4 and above.
# 1. Comment out, or remove the previous method which was: driver = webdriver.Chrome('chromedriver.exe path')
# 2. Add following code
s = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=s)

# initialize chrome driver object
# driver = webdriver.Chrome('./chromedriver.exe')  # relative path
# initialize chrome driver object
# driver = webdriver.Chrome(r'C:\Automation\PythonPRJ\moodle_app\chromedriver.exe')
# right-click chromedriver.exe, copy Path > Absolute Path


# ------------------ AOS WEB ELEMENTS ------------------------------
app = 'Advantage Online Shopping'
base_url = 'https://advantageonlineshopping.com/#/'
new_account_url = 'https://advantageonlineshopping.com/#/register'
new_account_page_title = 'CREATE NEW ACCOUNT'
home_page_title = '\xa0Advantage Shopping'
# -------------------------------------------------


def setUp():
    print(f'Launch {app}')
    print(f'----------------------------------------')
    driver.maximize_window()  # open web browser and maximize the window
    driver.implicitly_wait(30)  # wait for the browser response in general
    driver.get(base_url)  # navigate to app website

    # check the correct URL and the correct title
    if driver.current_url == base_url and driver.title == home_page_title:
        print(f'We\'re at {app} URL: {driver.current_url}')
        print('Actual Page Title: ', {driver.title})
        print(f'We\'re seeing page title: {driver.title}')
        # breakpoint()
    else:
        print(driver.current_url)
        print(f'We are not on {app} Home Page. Check your code')
        tearDown()


def tearDown():  # function to end the session
    if driver is not None:
        print(f'----------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        sleep(2)
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


def create_new_user():
    if driver.current_url == base_url:
        driver.find_element(By.ID, 'menuUserLink').click()
        sleep(2)
        assert driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT')
        driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()




setUp()
create_new_user()
#log_in()
#log_out()
tearDown()
