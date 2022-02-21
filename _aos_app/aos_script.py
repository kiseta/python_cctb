__author__ = 'tk'
import datetime
import sys
from time import sleep

from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

fake = Faker(locale=['en_CA', 'en_US'])

s = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=s)


# ------------------ AOS WEB ELEMENTS ------------------------------
app = 'Advantage Online Shopping'
base_url = 'https://advantageonlineshopping.com/#/'
new_account_url = 'https://advantageonlineshopping.com/#/register'
new_account_page_title = 'CREATE NEW ACCOUNT'
home_page_title = '\xa0Advantage Shopping'

first_name = fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'
user_name = f'{first_name}{last_name}'.lower()[:12]
password = 'Pass1'
user_email = f'{user_name}@{fake.free_email_domain()}'
phone = fake.bothify(text='1-(###)-###-####')
country = fake.current_country()
city = fake.city()[:10]
address = fake.street_address()
province = fake.province_abbr()
postal_code = fake.postalcode()
hr = f'\n------------------------~*~--------------------------'

list_name = ['usernameRegisterPage', 'emailRegisterPage', 'passwordRegisterPage', 'confirm_passwordRegisterPage',
             'first_nameRegisterPage', 'last_nameRegisterPage', 'phone_numberRegisterPage',
             'cityRegisterPage', 'addressRegisterPage', 'state_/_province_/_regionRegisterPage',
             'postal_codeRegisterPage']

list_val = [user_name, user_email, password, password,
            first_name, last_name, phone,
            city, address, province, postal_code]

print(list_val)
print(country)
# -------------------------------------------------


def wait(sec):
    driver.implicitly_wait(sec)


def setup():
    print(f'Launch {app}')
    print(hr)
    driver.maximize_window()  # open web browser and maximize the window
    driver.implicitly_wait(30)  # wait for the browser response in general
    driver.get(base_url)  # navigate to app website

    # check the correct URL and the correct title
    if driver.current_url == base_url and driver.title == home_page_title:
        print(f'Yey! {app} is launched! URL: {driver.current_url}')
        print('Page Title: ', {driver.title})
    else:
        print(driver.current_url)
        print(f'We are not on {app} Home Page. Check your code')
        teardown()


def teardown():  # function to end the session
    if driver is not None:
        print(f'Test Completed at: {datetime.datetime.now()}{hr}')
        sleep(2)
        driver.close()
        driver.quit()


def log_in():
    print(f'\n------------------------~* LOGIN  *~------------------------')
    if driver.current_url == base_url:
        wait(2)
        driver.find_element(By.ID, 'menuUserLink').click()
        sleep(2)
        assert driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').is_displayed()
        if driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').is_displayed():
            print(f'Login form is displayed - continue to Login{hr}')
            driver.find_element(By.NAME, 'username').send_keys(user_name)
            sleep(0.25)
            driver.find_element(By.NAME, 'password').send_keys(password)
            sleep(0.25)
            driver.find_element(By.ID, 'sign_in_btnundefined').click()
            sleep(0.25)
        else:
            print(f'Login Form is not displayed')


def validate_user_login():
    print(f'\n----------------~* VALIDATE NEW USER  *~----- ------------')
    if driver.find_element(By.LINK_TEXT, user_name).is_displayed():
        print(f'{user_name} Login Successful!{hr}')
        sleep(0.25)
    else:
        print(f'We\'re could not login. Try again.')


def log_out():
    print(f'\n------------------------~* LOGOUT  *~------------------------')
    driver.find_element(By.LINK_TEXT, user_name).click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//a/div/label[contains(.,"Sign out")]').click()
    sleep(0.25)
    if driver.current_url == base_url:
        print(f'Logout Successful! at {datetime.datetime.now()}{hr}')
    driver.refresh()
    wait(3)
    # breakpoint()


def create_new_user():
    print(f'\n-----------------~* CREATE NEW USER *~--------------------')
    if driver.current_url == base_url:
        driver.find_element(By.ID, 'menuUserLink').click()
        sleep(2)
        assert driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').is_displayed()
        print(f'Login form is displayed - continue to Create New Account{hr}')
        driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
        wait(5)
        if driver.current_url == new_account_url:
            assert driver.find_element(By.XPATH, '//h3[contains(.,"CREATE ACCOUNT")]').is_displayed()
            wait(5)
            print(f'CREATE ACCOUNT Page is displayed{hr}')
            # populate edit form fields
            for i in range(len(list_name)):
                name, val = list_name[i], list_val[i]
                driver.find_element(By.NAME, name).send_keys(val)
                wait(5)
            driver.find_element(By.NAME, 'i_agree').click()
            # wait(30)
            # driver.find_element(By.NAME, 'countryListboxRegisterPage').click()
            wait(0.25)
            #Select(driver.find_element(By.NAME, 'countryListboxRegisterPage')).select_by_visible_text('Canada')
            sleep(0.25)
            driver.find_element(By.ID, 'register_btnundefined').click()
            sleep(0.25)
            if driver.find_element(By.LINK_TEXT, user_name).is_displayed():
                print(f'New User {user_name}/{user_email} registration successful!'
                      f'\nUserName: {user_name} is displayed{hr}')
                logger('created')
                sleep(0.25)
            else:
                print(f'New User was not created. Try again.')


def delete_account():
    print(f'\n-----------------~* DELETE NEW USER *~---------------------')
    assert driver.find_element(By.LINK_TEXT, user_name).is_displayed()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, user_name).click()
    wait(5)
    driver.find_element(By.XPATH, '//a/div/label[contains(.,"My account")]').click()
    wait(20)
    if driver.find_element(By.XPATH, f'//label[contains(.,"{full_name}")]').is_displayed():
        print(f'Account details page for user: \'{full_name}\' is displayed{hr}')
        wait(5)
        driver.find_element(By.CLASS_NAME, 'deleteBtnText').click()
        wait(5)
        delete_popup = driver.find_element(By.CLASS_NAME, 'deleteAccountPopupContent').is_displayed()
        print(f'Delete popup is displayed: {delete_popup}')
        if delete_popup:
            driver.find_element(By.XPATH, "//div[contains(text(), 'yes')]").click()
            driver.implicitly_wait(3)
            assert driver.find_element(By.XPATH, "//*[contains(., 'deleted successfully')]").is_displayed()
            conf_screen = driver.find_element(By.XPATH, "//*[contains(., 'deleted successfully')]").is_displayed()
            print(f'Delete Confirmation screen is displayed: {conf_screen}')
            conf = driver.find_element(By.XPATH, "//p[contains(., 'deleted successfully')]").get_attribute('innerHTML')
            print(f'Confirmation message is displayed: {conf}')
            sleep(2)
            print(f'User {full_name}/{user_email} is deleted!{hr}')
            logger('deleted')
            sleep(2)
        else:
            print(f'Delete Popup is not displayed')
            driver.find_element(By.CLASS_NAME, 'deleteBtnText').click()
            wait(30)


def validate_user_deleted():
    print(f'\n------------~* CONFIRM USER DOES NOT EXIST  *~-------------')
    wait(2)
    error_label = driver.find_element(By.XPATH, '//label[contains(.,"Incorrect user name or password.")]').text
    if driver.find_element(By.XPATH, '//label[contains(.,"Incorrect user name or password.")]').is_displayed():
        print(f'Username/Password {user_name}/{password} is not found. Error: {error_label}')
        wait(0.25)
        # close login popup
        driver.find_element(By.XPATH, '//div[contains(@class,"closeBtn loginPopUpCloseBtn")]').click()
    else:
        print(error_label)
    wait(2)


def logger(action):
    # create variable to store the file content
    old_instance = sys.stdout
    log_file = open('message.log', 'a')  # open log file and append a record
    sys.stdout = log_file
    print(f'{user_email}\t'
          f'{user_name}\t'
          f'{password}\t'
          f'{datetime.datetime.now()}\t'
          f'{action}')
    sys.stdout = old_instance
    log_file.close()


setup()
create_new_user()
log_out()
log_in()
validate_user_login()
delete_account()
log_in()
validate_user_deleted()
teardown()
