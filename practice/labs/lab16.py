__author__ = 'tk'
import datetime
from time import sleep

from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

fake = Faker(locale='en_US')

# 1. Using Selenium WebDriver, open the web browser.
# 2. Maximize the browser window.
# 3. Navigate to web page URL - https://www.demoblaze.com/ (Links to an external site.)
# 4. Check URL and title are as expected.
# 5. On the page, find the Nexus 6 model and click on it.
# 6. Check Nexus 6 h2 title is displayed. Use assert.
# 7. Click by Add to Cart button. If you'll see an alert at the top, use this command - driver.switch_to.alert.accept()
# 8. Go to Cart at the top menu and click on it.
# 9. Check the order is displayed and click by Delete link.
# 10. Close the browser and display a user-friendly message.

# initialize chrome driver object
s = Service(executable_path='../../chromedriver.exe')
driver = webdriver.Chrome(service = s)

#driver = webdriver.Chrome('../../chromedriver.exe')


# ------------------ DEMOBLAZE WEB ELEMENTS ------------------------------
app = 'DEMOBLAZE'
base_url = 'https://www.demoblaze.com/index.html'
home_page_title = "STORE"
product = 'Nexus 6'
category_list = ['Phones', 'Laptops', 'Monitors']
product_list = ['Nexus 6','Sony xperia z5','Nokia lumia 1520']
product_url = 'https://www.demoblaze.com/prod.html?idp_=3'
username = fake.user_name()
password = fake.password()
hr = '--------~*~----------------~*~----------\n'
# -------------------------------------------------


def setUp():
    driver.maximize_window()  # open web browser and maximize the window
    driver.implicitly_wait(30)  # wait for the browser response in general
    driver.get(base_url)  # navigate to app website

    # check the correct URL and the correct title
    if driver.current_url == base_url and driver.title == home_page_title:
        assert driver.current_url == base_url
        assert driver.title == home_page_title
        print(f'{hr}Launch {app} Website\nURL: {driver.current_url}\nPage title: {driver.title}')
        # breakpoint()
    else:
        print(f'{hr}>>>> We are NOT on {app} Home Page. Check your code.')
        print(f'{hr}Expected URL: {base_url} \nActual URL: {driver.current_url}')
        print(f'{hr}Expected Page Title: {home_page_title} \nActual Page Title: {driver.title}')
        tearDown()


def tearDown():  # function to end the session
    if driver is not None:
        print(f'{hr}Test Completed at: {datetime.datetime.now()}')
        sleep(0.25)
        driver.close()
        driver.quit()


def add_to_cart():
    if driver.current_url == base_url:

        for product in product_list:
            driver.find_element(By.LINK_TEXT, product).click()
            sleep(2)
            assert driver.find_element(By.XPATH, f'//H2[contains(.,"{product}")]').is_displayed()
            print(f'{hr}Go to: {product} page;\nURL: {driver.current_url}')
            driver.find_element(By.LINK_TEXT, 'Add to cart').click()
            sleep(0.25)
            driver.switch_to.alert.accept()
            print(f'{hr}{product} is added to Shopping Cart')
            sleep(0.25)
            driver.find_element(By.ID, 'nava').click()
            sleep(0.25)

        driver.find_element(By.ID, 'cartur').click()
        print(f'{hr}Go to Shopping Cart')
        sleep(0.25)

        for product in product_list:
            assert driver.find_element(By.XPATH, f'//td[contains(.,"{product}")]').is_displayed()
            check = driver.find_element(By.XPATH, f'//td[contains(.,"{product}")]').is_displayed()
            print(f'{hr}Success! {product} is found in Shopping Cart: {check}')
            sleep(0.25)

        #driver.find_element(By.LINK_TEXT, 'Delete').click()
        driver.find_element(By.XPATH, f"//td[contains(., '{product_list[1]}')]/../td/a[contains(text(),'Delete')]").click()
        print(f'{hr}Now deleting {product_list[1]} from Shopping Cart')
        sleep(0.25)
        # Works but takes too long
        # try:
        #     assert driver.find_element(By.XPATH, f'//td[contains(.,"{product}")]').is_displayed()
        # except NoSuchElementException as err:
        #     print(f'Check if {product} is in the cart: {err}')
        # finally:
        #     print(f'Done checking {product} is no longer in the cart')

        print(f'{hr}{product_list[1]} is deleted!')
        sleep(0.25)


def sign_up():
    driver.find_element(By.LINK_TEXT, 'Sign up').click()
    sleep(0.25)
    assert driver.find_element(By.ID, 'signInModalLabel').is_displayed()
    sleep(0.25)
    driver.find_element(By.ID, 'sign-username').send_keys(username)
    sleep(0.25)
    driver.find_element(By.ID, 'sign-password').send_keys(password)
    sleep(0.25)
    driver.find_element(By.XPATH, '//button[contains(text(),"Sign up")]').click()
    sleep(0.25)
    driver.switch_to.alert.accept()

def log_in():
    driver.find_element(By.LINK_TEXT, 'Log in').click()
    sleep(0.25)
    assert driver.find_element(By.ID, 'logInModalLabel').is_displayed()
    sleep(0.25)
    driver.find_element(By.ID, 'loginusername').send_keys(username)
    sleep(0.25)
    driver.find_element(By.ID, 'loginpassword').send_keys(password)
    sleep(0.25)
    driver.find_element(By.XPATH, '//button[contains(text(),"Log in")]').click()
    sleep(0.25)
    # nameofuser
    print(driver.find_element(By.ID, 'nameofuser').get_attribute("text"))
    assert driver.find_element(By.XPATH, f'//a[contains(text(), "Welcome {username}")]').is_displayed()
    logincheck = driver.find_element(By.XPATH, f'//a[contains(text(),{username})]').is_displayed()
    print(f'Login is successful {username} username is displayed: {logincheck}')


def log_out():
    driver.find_element(By.LINK_TEXT, 'Log out').click()
    sleep(0.25)

setUp()
sign_up()
log_in()
add_to_cart()
log_out()
tearDown()
