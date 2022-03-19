import datetime
import sys
from time import sleep

from faker import Faker
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

fake = Faker(locale=['en_CA', 'en_US'])
s = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=s)

# ------------------ LOCATORS ------------------------------
app = 'Parabank'
base_url = 'https://parabank.parasoft.com/'
home_page_url = 'https://parabank.parasoft.com/parabank/index.htm'
home_page_title = 'ParaBank | Welcome | Online Banking'
register_page_url = 'https://parabank.parasoft.com/parabank/register.htm'
register_page_title = 'ParaBank | Register for Free Online Account Access'

firstname = fake.first_name()
lastname = fake.last_name()
fullname = f'{firstname} {lastname}'
address = fake.street_address()
city = fake.city()
state = fake.province_abbr()
postalcode = fake.postalcode()
phone = fake.pyint(111111111, 999999999)
ssn = fake.ssn()
# username = f'{firstname[:6]}{fake.pyint(111, 999)}'.lower()
username = f'{firstname}{lastname}{fake.pyint(111,999)}'.lower()
password = fake.password()

list_id = ['customer.firstName', 'customer.lastName', 'customer.address.street', 'customer.address.city',
           'customer.address.state', 'customer.address.zipCode', 'customer.phoneNumber', 'customer.ssn',
           'customer.username', 'customer.password', 'repeatedPassword']

list_val = [firstname, lastname, address, city, state, postalcode, phone, ssn, username, password, password]



# --------------END PARABANK LOCATORS ----------------------------

def setup():
    print(f'\n\nLaunch {app}')
    driver.delete_all_cookies()
    driver.maximize_window()  # open web browser and maximize the window
    driver.implicitly_wait(30)  # wait for the browser response in general
    driver.get(base_url)  # navigate to app website
    # check the correct URL and the correct title
    if driver.current_url == home_page_url and driver.title == home_page_title:
        print(f'Yey! {app} is launched!\nHome Page URL: {driver.current_url}\nHome Page Title: {driver.title}')
        sleep(0.25)
    else:
        print(driver.current_url)
        print(f'{app} did not launch. Check your code or application')
        teardown()


def teardown():  # function to end the session
    if driver is not None:
        print('\n------------------------~* DONE *~------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()


def log_in():
    print(f'\n------------------------~* LOGIN *~------------------------')
    assert driver.find_element(By.XPATH, '//form[contains(@name,"login")]').is_displayed()
    print(f'Login Customer Full Name: \'{fullname}\'\nUsername: {username}\nPassword: {password}')
    driver.find_element(By.NAME, 'username').send_keys(username)
    sleep(0.25)
    driver.find_element(By.NAME, 'password').send_keys(password)
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[contains(@value,"Log In")]').click()
    sleep(0.5)
    print('----------------------~* VALIDATE *~------------------------')
    #check_username()
    check_fullname()


def log_out():
    print(f'\n------------------------~* LOGOUT *~------------------------')
    driver.find_element(By.LINK_TEXT, 'Log Out').click()
    sleep(0.25)
    if driver.find_element(By.XPATH, '//h2[contains(.,"Customer Login")]').is_displayed():
        print(f'{username} Logout successful!')


def register():
    print(f'\n-----------------~* REGISTER *~--------------------')
    if driver.current_url == home_page_url:
        driver.find_element(By.LINK_TEXT, 'Register').click()
        sleep(0.25)
        assert driver.find_element(By.XPATH, '//h1[contains(.,"Signing up is easy!")]').is_displayed()
        print(f'Current URL: {driver.current_url}\nCurrent Page Title: {driver.title}')
        # breakpoint()
        if register_page_url in driver.current_url and driver.title == register_page_title:
            print(f'Fill out registration form, data:\n{list_val}')
            sleep(0.25)
            # populate edit form fields
            for i in range(len(list_id)):
                fid, val = list_id[i], list_val[i]
                driver.find_element(By.ID, fid).send_keys(val)
                sleep(0.25)
            # submit form data
            driver.find_element(By.XPATH, '//input[contains(@value,"Register")]').click()
            driver.implicitly_wait(30)
            print('-----------------~* VALIDATE *~--------------------')
            logger('created')
            check_username()
            check_fullname()
            #breakpoint()


def check_fullname():
    print('---------------- full name h1 heading ----------------------')
    driver.implicitly_wait(3)
    try:
        fullname_check = driver.find_element(By.XPATH, f'//p[contains(.,"Welcome")]').text
        print(f'Full name welcome validation : {"PASS ✔" if fullname in fullname_check else "FAIL ✖"}')
        print(f'Expected: Welcome {fullname}, Actual: {fullname_check}')
    except NoSuchElementException as e:
        print(f'Error has occurred: {e}')
        teardown()


def check_username():
    print('---------------- username paragraph ----------------------')
    driver.implicitly_wait(3)
    try:
        username_check = driver.find_element(By.XPATH, f'//H1[@class="title"]').text
        print(f'User name welcome validation - {"PASS ✔" if username in username_check else "FAIL ✖"}')
        print(f'Expected: Welcome {username}, Actual: {username_check}')
    except NoSuchElementException as e:
        print(f'Error has occurred: {e}')
        teardown()


def logger(action):
    # create variable to store the file content
    old_instance = sys.stdout
    log_file = open('../logs/parabank.log', 'a')  # open log file and append a record
    sys.stdout = log_file
    print(f'{username}\t'
          f'{password}\t'
          f'{datetime.datetime.now()}\t'
          f'{action}')
    sys.stdout = old_instance
    log_file.close()


# setup()
# register()
# log_out()
# log_in()
# log_out()
# teardown()
