__author__ = 'tk'
from time import sleep

from selenium import webdriver  # import webdriver

# ------------------------------------------------
moodle_url = 'http://52.39.5.126/'
moodle_home_page_title = 'Software Quality Assurance Testing'

#-------------------------------------------------


#---------------------------------------------------


# initialize chrome driver object
driver = webdriver.Chrome(r'C:\Automation\PythonPRJ\chromedriver.exe') # right-click chromdriver.exe, copy Path > Absolute Path

# open web browser and maximize the window
driver.maximize_window() # broweser window opens, ignore 'depricated' warning in console

# wait for the browser response in general
driver.implicitly_wait(30)

# navigate to Moodle application website
driver.get(moodle_url)
# driver.get('https://advantageonlineshopping.com/')

# check that we are on the correct UTL and the we see the correct title

# function to end the session ----------------------
def teardown():
    sleep(5)
    driver.close()
    driver.quit()
# --------------------------------------------------

if driver.current_url == moodle_url and driver.title == moodle_home_page_title:
    print(f'We\'re at Moodle Homepage URL -- {driver.current_url}')
    print(f'We\'re seeing page title -- {moodle_home_page_title}')
else:
    print(driver.current_url)
    print(f'We are not on Moodle Home Page. Check your code')
    teardown()

teardown()

