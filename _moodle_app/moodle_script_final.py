__author__ = 'tk'

import datetime
import sys
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import moodle_locators as locators

# This method solves the "DeprecateWarning" error that occurs in Selenium 4 and above.
# 1. Comment out, or remove the previous method which was: driver = webdriver.Chrome('chromedriver.exe path')
# 2. Add following code

s = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=s)
user_system_id = ''

# initialize chrome driver object
# driver = webdriver.Chrome('./chromedriver.exe')  # relative path
# initialize chrome driver object
# driver = webdriver.Chrome(r'C:\Automation\PythonPRJ\moodle_app\chromedriver.exe')
# right-click chromdriver.exe, copy Path > Absolute Path

# Method to open web browser
def setUp():
    print(f'Launch {locators.app}')
    print(f'----------------------------------------')
    driver.maximize_window()  # open web browser and maximize the window
    driver.implicitly_wait(30)  # wait for the browser response in general
    driver.get(locators.moodle_url)  # navigate to app website

    # check the correct URL and the correct title
    if driver.current_url == locators.moodle_url and driver.title == locators.moodle_home_page_title:
        print(f'Moodle Homepage URL:{driver.current_url} - Moodle Homepage title: {driver.title} ---')
    else:
        print(driver.current_url)
        print(f'We are not on Moodle Home Page. Check your code')
        tearDown()

# Method to close web browser
def tearDown():  # function to end the session
    if driver is not None:
        print(f'----------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        sleep(0.5)
        driver.close()
        driver.quit()

# Login with dynamic user name and password
def log_in(username, password):
    if driver.current_url == locators.moodle_url:
        driver.find_element(By.LINK_TEXT, 'Log in').click()
        if driver.current_url == locators.moodle_login_page_url:
            print(f'Navigate to Login Page - Page title: {driver.title} --- ')
            driver.find_element(By.ID, 'username').send_keys(username)
            sleep(0.25)
            driver.find_element(By.ID, 'password').send_keys(password)
            sleep(0.25)
            driver.find_element(By.ID, 'loginbtn').click()
            if driver.title == 'Dashboard' and driver.current_url == locators.moodle_dashboard_url:
                assert driver.current_url == locators.moodle_dashboard_url
                print(f'--- Navigate to Dashboard Page - Page Title: {driver.title} --- ')
                print(f'--- User: "{username}/{password}" login successful! --- ')
            else:
                print(f'We\'re not at the dashboard. Try again.')

# Logout method
def log_out():
    driver.find_element(By.CLASS_NAME, 'userpicture').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//span[contains(.,"Log out")]').click()
    sleep(0.25)
    if driver.current_url == locators.moodle_url:
        print(f'Logout Successful! at {datetime.datetime.now()}')
    # breakpoint()

#
def create_new_user():
    # Navigate to Site Administration > Users > Add New User
    driver.find_element(By.XPATH, '//span[contains(.,"Site administration")]').click()
    sleep(0.25)
    assert driver.find_element(By.LINK_TEXT, 'Users').is_displayed()
    driver.find_element(By.LINK_TEXT, 'Users').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Add a new user').click()
    sleep(0.25)
    # Assert we are on Add New User page
    assert driver.find_element(By.LINK_TEXT, 'Add a new user').is_displayed()
    sleep(0.25)
    print(f'--- Navigate to Add a new user Page - Page title: {driver.title} --- ')
    # Enter fake data into username field
    driver.find_element(By.ID, 'id_username').send_keys(locators.new_username)  #
    sleep(0.25)
    # click to activate password filed
    driver.find_element(By.LINK_TEXT, 'Click to enter text').click()
    sleep(0.25)
    # enter fake password
    driver.find_element(By.ID, 'id_newpassword').send_keys(locators.new_password)
    # enter first name
    driver.find_element(By.ID, 'id_firstname').send_keys(locators.first_name)
    # enter last name
    driver.find_element(By.ID, 'id_lastname').send_keys(locators.last_name)
    # enter email address
    driver.find_element(By.ID, 'id_email').send_keys(locators.email)
    # select an option 'Allow every one to see my email address'
    Select(driver.find_element(By.ID, 'id_maildisplay')).select_by_visible_text(
        'Allow everyone to see my email address')
    sleep(0.25)
    # enter moodle net profile
    driver.find_element(By.ID, 'id_moodlenetprofile').send_keys(locators.moodle_net_profile)
    sleep(0.25)
    # enter city
    driver.find_element(By.ID, 'id_city').send_keys(locators.city)
    sleep(0.25)
    # select an option 'Allow every one to see my email address'
    Select(driver.find_element(By.ID, 'id_country')).select_by_visible_text(locators.country)
    sleep(0.25)
    # select an option 'Allow every one to see my email address'
    Select(driver.find_element(By.ID, 'id_timezone')).select_by_visible_text('America/Vancouver')
    sleep(0.25)
    driver.find_element(By.ID, 'id_description_editoreditable').clear()
    driver.find_element(By.ID, 'id_description_editoreditable').send_keys(locators.description)
    sleep(0.25)

    # upload picture to the user picture session
    driver.find_element(By.CLASS_NAME, 'dndupload-arrow').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//span[contains(.,"Server files")]').click()
    sleep(0.25)

    # select an image to upload
    #img_path = ['System', 'Technology', 'Software Testing', 'Software Manual Testing', 'Course image','Mannual-Testing.jpg']
    img_path = ['System', 'sl_Frozen', 'sl_How to build a snowman', 'Course image', 'gieEd4R5T.png']
    #System sl_Frozen sl_How to build a snowman Course image
    # img_path = ['Private files', 'femaleyes.png']
    for p in img_path:
        # driver.find_element(By.XPATH, f'//span[contains(.,"{p}")]').click()
        driver.find_element(By.LINK_TEXT, p).click()
        sleep(0.25)

    driver.find_element(By.XPATH, '//input[@value="4"]').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//button[contains(.,"Select this file")]').click()
    sleep(0.25)
    # enter value to the picture description
    driver.find_element(By.ID, 'id_imagealt').send_keys(locators.pic_desc)

    driver.find_element(By.LINK_TEXT, 'Additional names').click()
    sleep(0.25)
    driver.find_element(By.ID, 'id_firstnamephonetic').send_keys(locators.first_name)
    driver.find_element(By.ID, 'id_lastnamephonetic').send_keys(locators.last_name)
    driver.find_element(By.ID, 'id_middlename').send_keys(locators.middle_name)
    driver.find_element(By.ID, 'id_alternatename').send_keys(locators.new_username)
    sleep(0.25)

    driver.find_element(By.LINK_TEXT, 'Interests').click()
    sleep(0.25)

    # add multiple insterests
    for tag in locators.list_of_interests:
        # driver.find_element(By.XPATH, '//div[3]/input').send_keys(tag)
        driver.find_element(By.XPATH, '//input[contains(@id, "form_autocomplete_input")]').send_keys(tag + "\n")
        sleep(0.25)
        # driver.find_element(By.XPATH, '//div[3]/input').send_keys(Keys.ENTER) # import Keys
        # driver.find_element(By.XPATH, '//input[contains(@id, "form_autocomplete_input")]').send_keys(Keys.ENTER)
        sleep(0.25)

    # for i in range(0, 3):
    #     driver.find_element(By.XPATH, '//input[contains(@id, "form_autocomplete_input")]').send_keys(locators.fake.job() + "\n")
    #     sleep(0.25)

    # populate optional fields
    # driver.find_element(By.LINK_TEXT, 'Optional').click()
    driver.find_element(By.XPATH, "//a[text() = 'Optional']").click()

    for i in range(len(locators.lst_ids)):
        fld, fid, val = locators.lst_opt[i], locators.lst_ids[i], locators.lst_val[i]
        # print(f'Populate \'{fld}\' field with \'{val}\' value -------------------------')
        # driver.find_element(By.ID, f'{fid}').send_keys(val)
        driver.find_element(By.ID, fid).send_keys(val)
        # other options
        # driver.find_element(By.CSS_SELECTOR, 'input#' + fid).send_keys(val)
        # driver.find_element(By.CSS_SELECTOR, f'input#{fid}').send_keys(val)
        # driver.find_element(By.XPATH, f'//*[@id="{fid}"]').send_keys(val)
        sleep(0.25)
    # breakpoint()
    driver.find_element(By.ID, 'id_submitbutton').click()
    sleep(0.25)
    print(f'--- New user "{locators.new_username}" is added.')


def search_user():
    # Check we are on the User's Main Page
    if driver.current_url == locators.moodle_users_main_page and driver.title == locators.moodle_users_main_page_title:
        assert driver.find_element(By.LINK_TEXT, "Browse list of users").is_displayed()
        print('\'Browse list of users\' page is displayed: ', driver.find_element(By.LINK_TEXT, "Browse list of users").is_displayed())
        if driver.find_element(By.ID, 'fgroup_id_email_grp_label').is_displayed() and \
                driver.find_element(By.NAME, 'email').is_displayed():
            sleep(0.25)
            print(f'--- Search for User by Email: "{locators.email}" --- ')
            driver.find_element(By.CSS_SELECTOR, 'input#id_email').send_keys(locators.email)
            sleep(0.25)
            driver.find_element(By.CSS_SELECTOR, 'input#id_addfilter').click()

            if driver.find_element(By.XPATH, f'//td[contains(.,"{locators.email}")]'):
                # capture new user system id
                href = driver.find_element(By.LINK_TEXT, locators.full_name).get_attribute("href")
                global user_system_id
                user_system_id = href[href.find('=') + 1 : href.rfind('&')]
                print(f'--- User: {locators.email}, System ID: {user_system_id} is found --- ')

                return user_system_id

            # breakpoint()


def check_new_user_can_login():
    if driver.current_url == locators.moodle_dashboard_url:
        if driver.find_element(By.XPATH, f'//span[contains(., "{locators.full_name}")]').is_displayed():
            print(f'--- User with the name {locators.full_name} is displayed. ---')
            logger('created')


def delete_user():
    # Navigate to Site Administration > Users > Browse list of users
    driver.find_element(By.XPATH, '//span[contains(.,"Site administration")]').click()
    sleep(0.25)
    assert driver.find_element(By.LINK_TEXT, 'Users').is_displayed()
    driver.find_element(By.LINK_TEXT, 'Users').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Browse list of users').click()
    sleep(0.25)
    assert driver.find_element(By.LINK_TEXT, 'Browse list of users').is_displayed()
    sleep(0.25)

    # Search for a user
    search_user()

    # validate that email address and the delete buttons are displayed
    # 1. ID
    # 2. NAME
    # 3. LINK, PARTIAL LINK
    # 4. XPATH
    # 5. CSS SELECTOR
    # how to build an XPATH locator:
    # f''
    # f'//a[]'
    # f'//a[contains()]'
    # f'//a[contains(@href,"")]'
    # f'//a[contains(@href,"delete=1234")]'
    #  driver.find_element(By.XPATH, f'//a[contains(@href,"delete={user_system_id}")]')
    if driver.find_element(By.XPATH, f'//td[contains(.,"{locators.email}")]').is_displayed and \
            driver.find_element(By.XPATH, f'//a[contains(@href,"delete={user_system_id}")]').is_displayed:
            #driver.find_element(By.CSS_SELECTOR, f"a[href*='delete={user_system_id}']").is_displayed:

        print('--- Delete Link:', driver.find_element(By.CSS_SELECTOR, f"a[href*='delete']").get_attribute("href"))
        #driver.find_element(By.CSS_SELECTOR, f"a[href*='delete={user_system_id}']").click()
        driver.find_element(By.XPATH, f'//a[contains(@href,"delete={user_system_id}")]').click()
        sleep(0.25)
        # delete user
        driver.find_element(By.XPATH, "//button[text()='Delete']").click() # option 1
        # driver.find_element(By.XPATH, "//*[contains(text(), 'Delete')]").click() # option 2 * means any tag
        # driver.find_element(By.XPATH, '//i[@title="Delete"]').click() # option 3# only for i html tag
        print(f'--- User {locators.email}, System ID {user_system_id} is deleted  at:{datetime.datetime.now()} --- ')
        logger('deleted')
    else:
        print(f'--- User {locators.email} not found --- ')

    sleep(0.25)

    # breakpoint()


def logger(action):
    # create variable to store the file content
    old_instance = sys.stdout
    log_file = open('message.log', 'a') # open log file and append a record
    sys.stdout = log_file
    print(f'{user_system_id}\t'
          f'{locators.email}\t'
          f'{locators.new_username}\t'
          f'{locators.new_password}\t'
          f'{datetime.datetime.now()}\t'
          f'{action}')
    sys.stdout = old_instance
    log_file.close()


def logger_fun():
    # create variable to store the file content
    old_instance = sys.stdout
    log_file = open('messageBKP.log', 'a') # open log file for appending (a) and append a record
    sys.stdout = log_file
    print(f'{datetime.datetime.now()}'
          f'\nEmail: {locators.email}'
          f'\nUsername, Password: {locators.new_username}, {locators.new_password}'
          f'\nMoodle ID:{user_system_id}'
          f'\n{"-----~*~-----" * 3}')
    sys.stdout = old_instance
    log_file.close()


# -------------------- CREATE A NEW USER -----------------------
setUp()  # Open Web Browser

print(f'\n--- Create New User Test  -----------------------------')

log_in(locators.moodle_username, locators.moodle_password)  # Login
create_new_user()  # Create New User
search_user()  # Check New User created
log_out()  # Logout

print(f'--- Create New User Test --- PASSED -----------------✔\n')
sleep(0.5)

# -------------------- LOGIN AS NEW USER -----------------------

# setUp() # Open Web Browser
print(f'\n--- Loging as New User Test  -----------------------------')

log_in(locators.new_username, locators.new_password)  # Login
check_new_user_can_login()  # check new user
log_out()  # Logout

print(f'--- Loging as New User Test --- PASSED ---------------✔\n')
sleep(0.5)

# ----------------------- DELETE USER -----------------------
print(f'\n--- Delete New User Test  -----------------------------')

log_in(locators.moodle_username, locators.moodle_password)  # Login
delete_user()  # delete user
log_out()  # Logout

print(f'--- Delete New User Test --- PASSED -------------------✔\n')

tearDown()  # Close browser

logger()