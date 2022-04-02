import datetime
from time import sleep
from selenium import webdriver  # import selenium to the file
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import moodle_locators as locators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select  # <--- add this import for drop down lists

s = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=s)


def setUp():
    print(f'Launch {locators.app} App')
    print(f'--------------------~* LAUNCH APP *~--------------------------')
    # make browswer full screen
    driver.maximize_window()
    # give browser up to 30 seconds to respond
    driver.implicitly_wait(30)
    # navigate to Moodle App website
    driver.get(locators.moodle_url)
    # check that Moodle URL and the home page title are as expected
    if driver.current_url == locators.moodle_url and driver.title == locators.moodle_home_page_title:
        print(f'Yey! {locators.app} App website launched successfully!')
        print(f'{locators.app} Homepage URL: {driver.current_url}, Homepage title: {driver.title}')
        sleep(0.25)
    else:
        print(f'{locators.app} did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url}, Page title: {driver.title}')
        tearDown()


def tearDown():
    if driver is not None:
        print(f'--------------------~* DONE! *~--------------------------')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(0.5)
        driver.close()
        driver.quit()


def log_in(username, password):
    print(f'--------------------~* LOGIN *~--------------------------')
    if driver.current_url == locators.moodle_url:  # check we are on the home page
        driver.find_element(By.LINK_TEXT, 'Log in').click()
        if driver.current_url == locators.moodle_login_page_url and driver.title == locators.moodle_login_page_title: # check we are on the login page
            print(f' --- {locators.app} App Login page is displayed! Continue to log in.')
            sleep(0.25)
            driver.find_element(By.ID, 'username').send_keys(username)
            sleep(0.25)
            driver.find_element(By.ID, 'password').send_keys(password)
            sleep(0.25)
            driver.find_element(By.ID, 'loginbtn').click() # method 1 using ID
            # validate login successfull - Dashboard page is displayed
            if driver.current_url == locators.moodle_dashboard_url and driver.title == locators.moodle_dashboard_title:
                assert driver.current_url == locators.moodle_dashboard_url
                assert driver.title == locators.moodle_dashboard_title
                print(f' --- Login is successful. {locators.app} Dashboard is displayed - Page title: {driver.title}')
            else:
                print(f'Dashboard is not displayed. Check your code or website and try again.')


def log_out():
    print(f'--------------------~* LOGOUT *~--------------------------')
    driver.find_element(By.CLASS_NAME, 'userpicture').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//span[contains(.,"Log out")]').click()
    sleep(0.25)
    if driver.current_url == locators.moodle_url:
        print(f' --- Logout successful! {datetime.datetime.now()}')


def create_new_user():
    print(f'------------------~* CREATE NEW USER *~---------------------')
    # Navigate to 'Add a new user' form
    driver.find_element(By.XPATH, '//span[contains(., "Site administration")]').click()
    sleep(0.25)
    assert driver.find_element(By.LINK_TEXT, 'Users').is_displayed()
    linkchek = driver.find_element(By.LINK_TEXT, 'Users').is_displayed()
    print(f' --- User link is displayed: {linkchek}')
    driver.find_element(By.LINK_TEXT, 'Users').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Add a new user').click()
    sleep(0.25)
    # Validate we are on 'Add a new user' page
    assert driver.find_element(By.LINK_TEXT, 'Add a new user').is_displayed()
    assert driver.title == locators.moodle_add_new_user_page_title
    print(f' --- Navigate to Add a new user page - Page Title: {driver.title}')
    sleep(0.25)
    driver.find_element(By.ID, 'id_username').send_keys(locators.new_username)
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Click to enter text').click()
    sleep(0.25)
    driver.find_element(By.ID, 'id_newpassword').send_keys(locators.new_password)
    sleep(0.25)
    driver.find_element(By.ID, 'id_firstname').send_keys(locators.first_name)
    sleep(0.25)
    driver.find_element(By.ID,'id_lastname').send_keys(locators.last_name)
    sleep(0.25)
    driver.find_element(By.ID, 'id_email').send_keys(locators.email)
    sleep(0.25)

    # non-mandatory fields
    Select(driver.find_element(By.ID, 'id_maildisplay')).select_by_visible_text('Allow everyone to see my email address')
    sleep(0.25)
    driver.find_element(By.ID, 'id_moodlenetprofile').send_keys(locators.moodle_net_profile)
    sleep(0.25)
    driver.find_element(By.ID, 'id_city').send_keys(locators.city)
    sleep(0.25)
    Select(driver.find_element(By.ID, 'id_country')).select_by_visible_text(locators.country)
    sleep(0.25)
    Select(driver.find_element(By.ID, 'id_timezone')).select_by_value('America/Vancouver')
    sleep(0.25)
    driver.find_element(By.ID, 'id_description_editoreditable').clear()
    driver.find_element(By.ID, 'id_description_editoreditable').send_keys(locators.description)
    sleep(0.5)

    # upload picture
    driver.find_element(By.CLASS_NAME, 'dndupload-arrow').click()
    img_path = ['Server files', 'sl_Frozen', 'sl_How to build a snowman', 'Course image', 'gieEd4R5T.png']
    for path in img_path:
        driver.find_element(By.LINK_TEXT, path).click()
        sleep(0.25)

    # select a radio button
    # method 2 - click the label attached to radio button
    driver.find_element(By.XPATH, '//label[contains(., "Create an alias/shortcut to the file")]').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//button[contains(text(), "Select this file")]').click()
    sleep(0.25)
    driver.find_element(By.ID, 'id_imagealt').send_keys(locators.pic_desc)
    sleep(0.25)
    # populate Additional names section
    driver.find_element(By.LINK_TEXT, 'Additional names').click()
    sleep(0.25)
    driver.find_element(By.ID, 'id_firstnamephonetic').send_keys(locators.first_name)
    sleep(0.25)
    driver.find_element(By.ID, 'id_lastnamephonetic').send_keys(locators.last_name)
    sleep(0.25)
    driver.find_element(By.ID, 'id_middlename').send_keys(locators.middle_name)
    sleep(0.25)
    driver.find_element(By.ID, 'id_alternatename').send_keys(locators.first_name)

    # populate list of Interests
    driver.find_element(By.LINK_TEXT, 'Interests').click()
    for i in range(3):
      driver.find_element(By.XPATH, '//input[contains(@id, "form_autocomplete_input")]').send_keys(locators.fake.job() + ',')
      sleep(0.25)

    # populate Optional fields
    driver.find_element(By.LINK_TEXT, 'Optional').click()
    sleep(0.25)
    for i in range(len(locators.lst_ids)):
        fid, val = locators.lst_ids[i], locators.lst_val[i]
        driver.find_element(By.ID, fid).send_keys(val)
        sleep(0.25)

    ###############################################
    #   PRESS SUBMIT BUTTON TO COMPLETE REGISTRATION
    driver.find_element(By.ID, 'id_submitbutton').click()
    sleep(0.5)
    assert driver.find_element(By.LINK_TEXT, 'Browse list of users').is_displayed()
    print(f' --- New user {locators.new_username}/{locators.new_password}/{locators.email} is added')
    ###############################################


def search_user():
    print(f'------------------~* SEARCH USER *~---------------------')
    if locators.moodle_users_main_page_url in driver.current_url and driver.title == locators.moodle_users_main_page_title:
        assert driver.find_element(By.LINK_TEXT, 'Browse list of users').is_displayed()
        print(f' --- Browse list of users page is displayed')
        if driver.find_element(By.ID, 'fgroup_id_email_grp_label').is_displayed() and driver.find_element(By.NAME,'email').is_displayed():
            sleep(0.25)
            print(f' --- Search for user by email {locators.email}')
            driver.find_element(By.CSS_SELECTOR, 'input#id_email').send_keys(locators.email)
            sleep(0.25)
            driver.find_element(By.CSS_SELECTOR, 'input#id_addfilter').click()
            driver.implicitly_wait(5)
            try:
                assert driver.find_element(By.XPATH, f'//td[contains(., "{locators.full_name}")]/../td[contains(., "{locators.email}")]').is_displayed()
                href = driver.find_element(By.LINK_TEXT, locators.full_name).get_attribute("href")
                locators.sysid = href[href.find('=') + 1: href.rfind('&')]
                print(f' --- User {locators.full_name} / {locators.email} / System id: {locators.sysid} is found! ---')
            except NoSuchElementException as nse:
                print(' --- Element is not found')
                print(f' --- {locators.email} user does not exist')


def check_new_user_can_login():
    print(f'------------------~* CHECK NEW USER CAN LOGIN *~---------------------')
    if driver.current_url == locators.moodle_dashboard_url:
        if driver.find_element(By.XPATH, f'//span[contains(., "{locators.full_name}")]').is_displayed():
            print(f' --- User with the name {locators.full_name} login is confirmed.')


def delete_user():
    print(f'------------------~* DELETE *~---------------------')
    # Navigate to Site Administration > Users Browse list of users
    driver.find_element(By.XPATH, '//span[contains(., "Site administration")]').click()
    sleep(0.25)
    assert driver.find_element(By.LINK_TEXT, 'Users').is_displayed()
    driver.find_element(By.LINK_TEXT, 'Users').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Browse list of users').click()
    sleep(0.25)
    # search for the user
    search_user()
    # delete user
    assert  driver.find_element(By.XPATH, f'//td[contains(., "{locators.full_name}")]/../td/a[contains(@href, "delete={locators.sysid}")]').is_displayed()
    driver.find_element(By.XPATH, f'//td[contains(., "{locators.email}")]/../td/a[contains(@href, "delete={locators.sysid}")]').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//button[text()="Delete"]').click()
    sleep(0.25)
    print(f' --- User {locators.email}, System ID: {locators.sysid} is deleted! --- ')
    print(f'-------------~* CONFIRM USER IS DELETED *~-----------------')
    # confirm delete
    driver.implicitly_wait(3)
    try:
        assert driver.find_element(By.XPATH, f'//td[contains(., "{locators.full_name}")]/../td[contains(., "{locators.email}")]').is_displayed()
    except NoSuchElementException as nse:
        print(f' --- Element is not found\n--- {locators.email} user does not exist')


# setUp()
# log_in(locators.admin_username, locators.admin_password)
# create_new_user()
# search_user()
# log_out()
# log_in(locators.new_username, locators.new_password)
# check_new_user_can_login()
# log_out()
# log_in(locators.admin_username, locators.admin _password)
# delete_user()
# log_out()
# tearDown()