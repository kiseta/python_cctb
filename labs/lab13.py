__author__ = 'tk'

from selenium import webdriver  # import webdriver
from time import sleep

# -------------PAGE ELEMENTS SECTION -----------------------------------
base_url = 'https://www.google.ca/'
home_page_title = 'Google'

# -----------------------------------------------------------------------
# initialize chrome driver object
driver = webdriver.Chrome(r'C:\Automation\PythonPRJ\chromedriver.exe')  # right-click chromdriver.exe, copy Path > Absolute Path

# open web browser and maximize the window
driver.maximize_window()  # browser window opens, ignore 'deprecated' warning in console

# wait for the browser response in general
driver.implicitly_wait(30)

# navigate to application website
driver.get(base_url)


# check that we are on the correct URL and we see the correct title

# function to end the session ----------------------
def teardown():
    sleep(5)
    driver.close()
    driver.quit()
# --------------------------------------------------


if driver.current_url == base_url and driver.title == home_page_title:
    print(f'We\'re at website Homepage URL -- {driver.current_url}')
    print(f'We\'re seeing page title -- {driver.title}')
else:
    print(driver.current_url)
    print(f'We are not on {home_page_title}. Check your code')
    teardown()

teardown()
