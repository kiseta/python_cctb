import datetime
from time import sleep

from faker import Faker

from selenium import webdriver  # import selenium to the file
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

fake = Faker(locale='en_CA')

# Moodle Test Automation Plan
# launch Moodle App website - validate we are on the home page
# navigate to Login Screen - validate we are on the login page
# login with admin acount - validate we are on the Dashboard page
# navigate to Add New User page - validate we are on the Add New User page
# populate the new user form using Faker fake data
# submit the form - validate we are on the Browse List of Users page
# search for new user - validate new user is found
# logout from admin account
# login with new user credentials - validate new user can login
# logout from new user account
# login with admin acount
# search for a new user
# delete new user

# This method solves the "DeprecateWarning" error that occurs in Selenium 4 and above.
# 1. Comment out, or remove the previous method which was: driver = webdriver.Chrome('chromedriver.exe path')
# 2. Add following code
s = Service(executable_path='../../chromedriver.exe')
driver = webdriver.Chrome(service=s)

# create a Chrome driver instance, specify path to chromedriver file
# driver = webdriver.Chrome('../../chromedriver.exe')


#------------------ locators section-------------------------------
app = 'Moodle'
admin_username = 'tkuser'
admin_password = 'Moodle!123'
moodle_url = 'http://52.39.5.126/'
moodle_home_page_title = 'Software Quality Assurance Testing'
moodle_login_page_url = 'http://52.39.5.126/login/index.php'
moodle_login_page_title = 'Software Quality Assurance Testing: Log in to the site'
moodle_dashboard_url = 'http://52.39.5.126/my/'
moodle_dashboard_page_title = 'Dashboard'
moodle_add_new_user_page_title = 'SQA: Administration: Users: Accounts: Add a new user'

# -------------------- data section ---------------------------------
first_name = fake.first_name()
last_name = fake.last_name()
middle_name = fake.first_name()

new_username = f'{first_name}{last_name}'.lower()
new_password = fake.password()
email = f'{new_username}@{fake.free_email_domain()}'
email1 = fake.email()

print(first_name, last_name, middle_name, new_username, new_password, email, email1)

# ----------------------------------------------------------
def setUp():
    print(f'Launch {app} App')
    print('--------------------~*~--------------------')
    # Make browser full screen
    driver.maximize_window()
    # Give browser up to 30 seconds to respond
    driver.implicitly_wait(30)
    # Navigate to Moodle app website
    driver.get(moodle_url)
    # Check that Moodle URL and the home page title are displayed
    if driver.current_url == moodle_url and driver.title == moodle_home_page_title:
        print(f'Yey! {app} Launched Successfully')
        print(f'{app} homepage URL: {driver.current_url}\nHome Page Title: {driver.title}')
        sleep(0.25)
    else:
        print(f'{app}  did not launch. Check your code or application!')
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
    if driver.current_url == moodle_url: # check we are on the home page
        print(f'Login Link is displayed: {driver.find_element(By.LINK_TEXT, "Log in").is_displayed()}')
        driver.find_element(By.LINK_TEXT, 'Log in').click()
        if driver.current_url == moodle_login_page_url: # check we are on the login page
            print(f'--- {app} App Login Page is displayed!')
            sleep(0.25)
            driver.find_element(By.ID, 'username').send_keys(admin_username)
            sleep(0.25)
            driver.find_element(By.ID, 'password').send_keys(admin_password)
            sleep(0.25)
            driver.find_element(By.ID, 'loginbtn').click()
            # validate we are at the Dashboard
            if driver.title == moodle_dashboard_page_title and driver.current_url == moodle_dashboard_url:
                assert driver.current_url == moodle_dashboard_url
                assert driver.title == moodle_dashboard_page_title
                print(f'--- Login Successful. {app} Dashboard is displayed - Page title: {driver.title}')
            else:
                print(f'Dashboard is not displayed. Check your code and try again.')


def log_out():
    driver.find_element(By.CLASS_NAME, 'userpicture').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//span[contains(.,"Log out")]').click()
    sleep(0.25)
    # validate logout successful
    if driver.current_url == moodle_url:
        print(f'--- Logout Successful! at {datetime.datetime.now()}')


def create_new_user():
    # navigate to Site Admin
    driver.find_element(By.XPATH,'//span[contains(.,"Site administration")]').click()
    sleep(0.25)
    assert driver.find_element(By.LINK_TEXT, 'Users').is_displayed()
    driver.find_element(By.LINK_TEXT, 'Users').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Add a new user').click()
    sleep(0.25)
    # validate we are on 'Add a new user page'
    assert driver.find_element(By.LINK_TEXT, 'Add a new user').is_displayed()
    assert driver.title == moodle_add_new_user_page_title
    print(f'--- Navigate to Add a New user Page - Page Title: {driver.title}')
    sleep(0.25)
    driver.find_element(By.ID, 'id_username').send_keys(new_username)
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Click to enter text').click()
    sleep(0.25)
    driver.find_element(By.ID, 'id_newpassword').send_keys(new_password)

    breakpoint()


setUp()
log_in()
create_new_user()
log_out()
tearDown()