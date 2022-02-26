import datetime
from time import sleep

from selenium import webdriver  # import selenium to the file
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Moodle Test Automation Plan
# launch Moodle App website - validate we are on the home page
# navigate to Login Screen - validate we are on the login page
# login with admin acount - validate we are on the Dashboard page
# navigate to Add new User page - validate
# populate the new user form using Faker fake data
# submit the form - validate
# search for new user - validate
# logout
# login with new user credentials - validate
# logout
# login with admin acount
# search for a new user
# delete new user

# This method solves the "DeprecateWarning" error that occurs in Selenium 4 and above.
# 1. Comment out, or remove the previous method which was: driver = webdriver.Chrome('chromedriver.exe path')
# 2. Add following code
s = Service(executable_path='../../chromedriver.exe')
driver = webdriver.Chrome(service = s)

# create a Chrome driver instance, specify path to chromedriver file
# driver = webdriver.Chrome('../../chromedriver.exe')


def setUp():
    print(f'Launch Moodle App')
    print('--------------------~*~--------------------')
    # Make browser full screen
    driver.maximize_window()
    # Give browser up to 30 seconds to respond
    driver.implicitly_wait(30)
    # Navigate to Moodle app website
    driver.get('http://52.39.5.126/')
    # Check that Moodle URL and the home page title are displayed
    if driver.current_url == 'http://52.39.5.126/' and driver.title == 'Software Quality Assurance Testing':
        print('Yey! Moodle Launched Successfully')
        print(f'Moodle homepage URL: {driver.current_url}\nHome Page Title: {driver.title}')
        sleep(0.25)
    else:
        print(f'Mooodle did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url}, Page Title: {driver.title}')
        tearDown()


def tearDown(): #
    if driver is not None:
        print('--------------------~*~--------------------')
        print(f'The test Completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()

# login to Moodle
def log_in():
    if driver.current_url == 'http://52.39.5.126/': # check we are on the home page
        driver.find_element(By.LINK_TEXT, 'Log in').click()
        if driver.current_url == 'http://52.39.5.126/login/index.php': # check we are on the login page
            print('Moodle App Login Page is displayed!')
            sleep(0.25)
            driver.find_element(By.ID, 'username').send_keys('cctbuser')
            sleep(0.25)
            driver.find_element(By.ID, 'password').send_keys('Moodle!123')
            sleep(0.25)
            driver.find_element(By.ID, 'loginbtn').click()
            # validate we are at the Dashboard
            if driver.title == 'Dashboard' and driver.current_url == 'http://52.39.5.126/my/':
                assert driver.current_url == 'http://52.39.5.126/my/'
                assert driver.title == 'Dashboard'
                print(f'Login Successful. Moodle Dashboard is displayed - Page title: {driver.title}')
            else:
                print(f'Dashboard is not displayed. Check your code and try again.')



setUp()
log_in()
tearDown()

