import datetime
from time import sleep

import moodle_locators as locators
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  # <------ add this import for drop down lists

s = Service(executable_path='../../../chromedriver.exe')


driver = webdriver.Chrome(service=s)


# Fixture method - to open web browser
def setUp():
    # Make a full screen
    driver.maximize_window()

    # Let's wait for the browser response in general
    driver.implicitly_wait(30)

    # Navigating to the Moodle app website
    driver.get(locators.moodle_url)

    # Checking that we're on the correct URL address and we're seeing correct title
    if driver.current_url == locators.moodle_url and driver.title == 'Software Quality Assurance Testing':
        print(f'We\'re at Moodle homepage -- {driver.current_url}')
        print(f'We\'re seeing title message -- "Software Quality Assurance Testing"')
    else:
        print(f'We\'re not at the Moodle homepage. Check your code!')
        driver.close()
        driver.quit()


def tearDown():
    if driver is not None:
        print(f'--------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()


def log_in():
    if driver.current_url == locators.moodle_url:
        driver.find_element(By.LINK_TEXT, 'Log in').click()
        if driver.current_url == locators.moodle_login_page_url:
            driver.find_element(By.ID, 'username').send_keys(locators.moodle_username)
            sleep(0.25)
            driver.find_element(By.ID, 'password').send_keys(locators.moodle_password)
            sleep(0.25)
            driver.find_element(By.ID, 'loginbtn').click()  # method 1, by ID
            # driver.find_element(By.XPATH, '//button[contains(.,"Log in")]').click()  # method 2, by XPATH any property
            # driver.find_element(By.XPATH, '//button[contains(@id, "loginbtn")]').click()  # method 3, by XPATH using contains id property
            # driver.find_element(By.XPATH, '//button[@id="loginbtn"]').click()
            # driver.find_element(By.XPATH, '//*[@id="loginbtn"]').click()
            # driver.find_element(By.CSS_SELECTOR, 'button[id*="loginbtn"]').click()
            # driver.find_element(By.CSS_SELECTOR, 'button#loginbtn').click()
            sleep(0.25)
            #breakpoint()
            if driver.title == 'Dashboard' and driver.current_url == locators.moodle_dashboard_url:
                assert driver.current_url == locators.moodle_dashboard_url
                print(f'Log in successfully. Dashboard is present')
            else:
                print(f'We\re not at the Dashboard. Try again')


def log_out():
    driver.find_element(By.CLASS_NAME, 'userpicture').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//span[contains(., "Log out")]').click()
    sleep(0.25)
    if driver.current_url == locators.moodle_url:
        print(f'Log out successfully at: {datetime.datetime.now()}')


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
    # select an option 'America/Vancouver' <-- give this as assignment to students
    Select(driver.find_element(By.ID, 'id_timezone')).select_by_visible_text('America/Vancouver')
    sleep(0.25)
    driver.find_element(By.ID, 'id_description_editoreditable').clear()
    driver.find_element(By.ID, 'id_description_editoreditable').send_keys(locators.description)
    sleep(0.25)

    # upload picture to the user picture session
    driver.find_element(By.CLASS_NAME, 'dndupload-arrow').click()
    sleep(0.25)
    # driver.find_element(By.XPATH, '//span[contains(.,"Server files")]').click()
    # sleep(0.25)

    # select an image to upload
    # img_path = ['System', 'Technology', 'Software Testing', 'Software Manual Testing', 'Course image','Mannual-Testing.jpg']
    img_path = ['Server files', 'System', 'sl_Frozen', 'sl_How to build a snowman', 'Course image', 'gieEd4R5T.png']
    for p in img_path:
        # driver.find_element(By.XPATH, f'//span[contains(.,"{p}")]').click()
        driver.find_element(By.LINK_TEXT, p).click()
        sleep(0.25)

    # select radio button: 2 options (use one) using input tag, or label tag
    # driver.find_element(By.XPATH, '//input[@value="4"]').click()
    driver.find_element(By.XPATH, '//label[contains(.,"Create an alias/shortcut to the file")]').click()
    sleep(0.25)

    breakpoint()

    driver.find_element(By.XPATH, '//button[contains(.,"Select this file")]').click()
    sleep(0.25)
    # enter value to the picture description
    driver.find_element(By.ID, 'id_imagealt').send_keys(locators.pic_desc)

    # populate additional names section
    driver.find_element(By.LINK_TEXT, 'Additional names').click()
    sleep(0.25)
    driver.find_element(By.ID, 'id_firstnamephonetic').send_keys(locators.first_name)
    driver.find_element(By.ID, 'id_lastnamephonetic').send_keys(locators.last_name)
    driver.find_element(By.ID, 'id_middlename').send_keys(locators.middle_name)
    driver.find_element(By.ID, 'id_alternatename').send_keys(locators.new_username)
    sleep(0.25)

    driver.find_element(By.LINK_TEXT, 'Interests').click()
    sleep(0.25)

    # add multiple interests
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

    breakpoint()


# Open web browser
setUp()
# Log in
log_in()
# Create a new user
create_new_user()
# Log out
log_out()
# Close the web browser
tearDown()