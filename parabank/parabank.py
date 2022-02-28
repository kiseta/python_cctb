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
phone = fake.bothify(text='1-(###)-###-####')
ssn = fake.ssn()
username = f'{firstname}{lastname}'.lower() # fake.user_name()
password = fake.password()
user_email = f'{username}@{fake.free_email_domain()}'
email = fake.free_email()

hr = f'\n------------------------~*~--------------------------'

list_fld_id = ['customer.firstName','customer.lastName','customer.address.street','customer.address.city',
                 'customer.address.state','customer.address.zipCode','customer.phoneNumber','customer.ssn',
                 'customer.username','customer.password','repeatedPassword']

list_fld_val = [firstname, lastname, address, city, state, postalcode, phone, ssn, username, password, password]


print(list_fld_val)

# -------------------------------------------------



def setup():
    print(f'Launch {app}')
    print(hr)
    driver.maximize_window()  # open web browser and maximize the window
    driver.implicitly_wait(30)  # wait for the browser response in general
    driver.get(base_url)  # navigate to app website

    # check the correct URL and the correct title
    if driver.current_url == home_page_url and driver.title == home_page_title:
        print(f'Yey! {app} is launched!\n Home Page URL: {driver.current_url}\nHome Page Title: {driver.title}')
        sleep(5)
    else:
        print(driver.current_url)
        print(f'{app} did not launch. Check your code or application')
        teardown()


def teardown():  # function to end the session
    if driver is not None:
        print(f'Test Completed at: {datetime.datetime.now()}{hr}')
        sleep(2)
        driver.close()
        driver.quit()


def log_in():
    print(f'\n------------------------~* LOGIN *~------------------------')
    assert driver.find_element(By.XPATH, '//form[contains(@name,"login")]').is_displayed()
    driver.find_element(By.NAME, 'username').send_keys(username)
    sleep(0.25)
    driver.find_element(By.NAME, 'password').send_keys(password)
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[contains(@value,"Log In")]').click()
    sleep(0.25)


def validate_login():
    print(f'\n----------------~* VALIDATE LOGIN *~------------------')
    if driver.find_element(By.XPATH, f'//p[contains(.,"Welcome {fullname}")]').is_displayed():
        print(f'{username} Login Successful!{hr}')
        sleep(0.25)
    else:
        print(f'We\'re could not login. Try again.{hr}')


def log_out():
    print(f'\n------------------------~* LOGOUT *~------------------------')
    driver.find_element(By.LINK_TEXT, 'Log Out').click()
    sleep(0.25)
    if driver.find_element(By.XPATH, '//h2[contains(.,"Customer Login")]').is_displayed():
        print(f'{username} Logout successful!{hr}')

    # breakpoint()


def register():
    #global element
    print(f'\n-----------------~* REGISTRATION *~--------------------')
    if driver.current_url == home_page_url:
        driver.find_element(By.LINK_TEXT, 'Register').click()
        sleep(0.25)
        assert driver.find_element(By.XPATH, '//h1[contains(.,"Signing up is easy!")]').is_displayed()
        print(f'Current URL: {driver.current_url}\nCurrent Page Title: {driver.title}')
        #breakpoint()
        if register_page_url in driver.current_url and driver.title == register_page_title:
            print(f'Fill out registration form {hr}')
            sleep(0.25)
            # populate edit form fields
            for i in range(len(list_fld_id)):
                fld_id, fld_val = list_fld_id[i], list_fld_val[i]
                driver.find_element(By.ID, fld_id).send_keys(fld_val)
                sleep(0.25)
            driver.find_element(By.XPATH, '//input[contains(@value,"Register")]').click()
            driver.implicitly_wait(30)
            chk1 = driver.find_element(By.XPATH, f'//p[contains(.,"{fullname}")]').is_displayed()
            chk2 = driver.find_element(By.XPATH, f'//h1[contains(text(),"Welcome {username}")]').is_displayed()
            #breakpoint()
            if chk1 and chk2:
                print(f'Registration successful: Confirmation Full Name: {chk1}, Confirmation username: {chk2}')
                print(f'User registered: {username}/{password}{hr}')
                logger('created')
                sleep(0.25)
            else:
                print(f'New User was not created. Try again.')


def logger(action):
    # create variable to store the file content
    old_instance = sys.stdout
    log_file = open('message.log', 'a')  # open log file and append a record
    sys.stdout = log_file
    print(f'{username}\t'
          f'{password}\t'
          f'{datetime.datetime.now()}\t'
          f'{action}')
    sys.stdout = old_instance
    log_file.close()


setup()
register()
log_out()
log_in()
validate_login()
log_out()
teardown()
