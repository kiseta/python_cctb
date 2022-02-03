__author__ = 'tk'

import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import moodle_locators as locators

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


def setUp():
    print(f'Launch {locators.app}')
    print(f'----------------------------------------')
    driver.maximize_window()  # open web browser and maximize the window
    driver.implicitly_wait(30)  # wait for the browser response in general
    driver.get(locators.moodle_url)  # navigate to app website

    # check the correct URL and the correct title
    if driver.current_url == locators.moodle_url and driver.title == locators.moodle_home_page_title:
        print(f'We are at Moodle Homepage URL -- {driver.current_url}')
        print(f'We are seeing page title -- {driver.title}')
    else:
        print(driver.current_url)
        print(f'We are not on Moodle Home Page. Check your code')
        tearDown()


def tearDown():  # function to end the session
    if driver is not None:
        print(f'----------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()


def log_in():
    if driver.current_url == locators.moodle_url:
        driver.find_element(By.LINK_TEXT, 'Log in').click()
        if driver.current_url == locators.moodle_login_page_url:
            print('We are at the Login Page!')
            driver.find_element(By.ID, 'username').send_keys(locators.moodle_username)
            sleep(0.25)
            driver.find_element(By.ID, 'password').send_keys(locators.moodle_password)
            sleep(0.25)
            driver.find_element(By.ID, 'loginbtn').click()
            if driver.title == 'Dashboard' and driver.current_url == locators.moodle_dashboard_url:
                assert driver.current_url == locators.moodle_dashboard_url
                print(f'Login Successful. Moodle Dashboard is displayed - Page Title: {driver.title}')
            else:
                print(f'We\'re not at the dashboard. Try again.')


def log_out():
    driver.find_element(By.CLASS_NAME, 'userpicture').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//span[contains(.,"Log out")]').click()
    sleep(0.25)
    if driver.current_url == locators.moodle_url:
        print(f'Logout Successful! at {datetime.datetime.now()}')
    # breakpoint()

def create_new_user():
    # Navigate to Site Administration
    driver.find_element(By.XPATH, '//span[contains(.,"Site administration")]').click()
    sleep(0.25)
    assert driver.find_element(By.LINK_TEXT, 'Users').is_displayed()
    driver.find_element(By.LINK_TEXT, 'Users').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Add a new user').click()
    sleep(0.25)
    assert driver.find_element(By.LINK_TEXT, 'Add a new user').is_displayed()
    sleep(0.25)
    # Enter fake data into username field
    driver.find_element(By.ID, 'id_username').send_keys(locators.new_username) #
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
    Select(driver.find_element(By.ID, 'id_maildisplay')).select_by_visible_text('Allow everyone to see my email address')
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
    driver.find_element(By.CLASS_NAME,'dndupload-arrow').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//span[contains(.,"Server files")]').click()
    sleep(0.25)

    # select an image to upload
    img_path = ['System','Technology','Software Testing','Software Manual Testing','Course image','Mannual-Testing.jpg' ]
    #img_path = ['Private files', 'femaleyes.png']
    for p in img_path:
        #driver.find_element(By.XPATH, f'//span[contains(.,"{p}")]').click()
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

    # add multiple insteres
    for tag in locators.list_of_interests:
        #driver.find_element(By.XPATH, '//div[3]/input').send_keys(tag)
        driver.find_element(By.XPATH, '//input[contains(@id, "form_autocomplete_input")]').send_keys(tag)
        sleep(0.25)
        #driver.find_element(By.XPATH, '//div[3]/input').send_keys(Keys.ENTER) # import Keys
        driver.find_element(By.XPATH, '//input[contains(@id, "form_autocomplete_input")]').send_keys(Keys.ENTER)
        sleep(0.25)

    # populate optional fields
    # driver.find_element(By.LINK_TEXT, 'Optional').click()
    driver.find_element(By.XPATH, "//a[text() = 'Optional']").click()

    for i in range(len(locators.lst_ids)):
        fld, fid, val = locators.lst_opt[i], locators.lst_ids[i], locators.lst_val[i]
        print(f'Populate \'{fld}\' field with \'{val}\' value -------------------------')
        #driver.find_element(By.ID, f'{fid}').send_keys(val)
        driver.find_element(By.ID, fid).send_keys(val)
        # other options
        # driver.find_element(By.CSS_SELECTOR, 'input#' + fid).send_keys(val)
        #driver.find_element(By.CSS_SELECTOR, f'input#{fid}').send_keys(val)
        #driver.find_element(By.XPATH, f'//*[@id="{fid}"]').send_keys(val)
        sleep(0.25)

    driver.find_element(By.ID, 'id_submitbutton').click()
    sleep(5)
    breakpoint()

# Open Web Browser
setUp()
# Login
log_in()
# Create New User
create_new_user()
# Logout
log_out()
# Close browser
tearDown()