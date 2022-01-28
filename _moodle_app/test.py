import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('../chromedriver.exe')


# Fixture method - to open web browser
def setUp():
    # Make a full screen
    driver.maximize_window()

    # Let's wait for browser response in general
    driver.implicitly_wait(30)

    # Navigating to the moodle application website
    driver.get('http://52.39.5.126/')

    # Checking the we're in the current url address and we're seeing correct title
    if driver.current_url == 'http://52.39.5.126/' and driver.title ==  'Software Quality Assurance Testing':
        print(f'We are at Moodle homepage -- {driver.current_url}')
        print(f'We\'re seeing title message -- "Software Quality Assurance Testing"')
        #sleep(5)
        #driver.close()
    else:
        print(f'We are at Moodle homepage. Check your code!')
        driver.close()
        driver.quit()
def tearDown():
    if driver is not None:
        print(f'----------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()


def log_in():
    if driver.current_url == 'http://52.39.5.126/':
        driver.find_element(By.LINK_TEXT, 'Log in').click()
        if driver.current_url == 'http://52.39.5.126/login/index.php':
            driver.find_element(By.ID, 'username').send_keys('Fernandodupa')
            sleep(0.25)
            driver.find_element(By.ID, 'password').send_keys('Moodle50#')
            sleep(0.25)
            driver.find_element(By.ID, 'loginbtn').click()
            if driver.title == 'Dashboard' and driver.current_url == 'http://52.39.5.126/my/':
                assert driver.current_url == 'http://52.39.5.126/my/'
                print('Log in successfully. Dashboard is present')
            else:
                print(f'We are not at the Dashboard. Try again')


def log_out():
    driver.find_element(By.CLASS_NAME, 'userpicture').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//span[contains(.,"Log out")]').click()
    sleep(0.25)
    if driver.current_url == 'http://52.39.5.126/':
        print(f'Log out successfully at: {datetime.datetime.now()}')





setUp()
log_in()
log_out()
tearDown()
