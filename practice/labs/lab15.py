__author__ = 'tk'
import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# ------------------------------------------------
app = "Wikipedia"
base_url = 'https://en.wikipedia.org/wiki/Main_Page'
home_page_title = 'Wikipedia, the free encyclopedia'
search_term = 'Python (programming language)'
search_term_url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
search_term_page_title = 'Python (programming language) - Wikipedia'
hr = '--------------------------------------------\n' # horizontal rule divider
#-------------------------------------------------

s = Service(executable_path='../../chromedriver.exe')
driver = webdriver.Chrome(service=s)


def setUp():
    print(f'Launch {app}!')
    driver.maximize_window()  # open web browser and maximize the window
    driver.implicitly_wait(30)  # wait for the browser response in general
    driver.get(base_url)  # navigate to app website

    # check the correct URL and the correct title
    if driver.current_url == base_url and driver.title == home_page_title:
        assert driver.current_url == base_url
        assert driver.title == home_page_title
        print(f'{hr}We are at {app} Homepage URL: {driver.current_url}')
        print(f'We are seeing page title:  {driver.title}')
    else:
        print(f'>>>> We are NOT on {app} Home Page. Check your code.')
        print(f'Expected URL: {base_url} \nActual URL: {driver.current_url}')
        print(f'Expected Page Title: {home_page_title} \nActual Page Title: {driver.title}')



def tearDown():
    if driver is not None:
        print(f'{hr}Test Completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()


def search():
    if driver.current_url == base_url and driver.title == home_page_title:
        assert driver.current_url == base_url
        assert driver.title == home_page_title
        # Search for search term
        print(f'{hr}Search for: {search_term}')
        driver.find_element(By.ID, 'searchInput').send_keys(search_term)
        sleep(2)
        driver.find_element(By.XPATH, f'//span[contains(.,"{search_term}")]').click()
        sleep(1)
        if driver.title == search_term_page_title and driver.current_url == search_term_url:
            assert driver.current_url == search_term_url
            assert driver.title == search_term_page_title
            print(f'We are at {search_term} Page!')
        else:
            print(f'>>>> We are NOT at {search_term_page_title} Page. Try again.')
            print(f'Expected URL: {search_term_url}; \nActual URL: {driver.current_url}')
            print(f'Expected Page Title: {search_term_page_title} \nActual Page Title: {driver.title}')
    else:
        print(f'>>>> We are NOT on {app} Home Page. Check your code.')
        print(f'Expected URL: {base_url}; \nActual URL: {driver.current_url}')
        print(f'Expected Page Title: {home_page_title} \nActual Page Title: {driver.title}')



def goHome():
    print(f'{hr}Navigate to {app} home page')
    driver.find_element(By.ID, 'p-logo').click()

setUp()
search()
goHome()
tearDown()