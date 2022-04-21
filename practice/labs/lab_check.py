
import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(executable_path='chromedriver')
driver = webdriver.Chrome(service=s)


app = 'PRODUCT STORE'
app1 = 'Nexus 6'
app3 = 'Cart'
item_list = ['Samsung galaxy s6', 'Nexus 6', 'Sony xperioa z5']
demo_url = 'https://www.demoblaze.com/index.html'
demo_home_page_title = 'STORE'
demo_nexus_dashboard_url = 'https://www.demoblaze.com/prod.html?idp_=3'
sony_url = 'https://www.demoblaze.com/prod.html?idp_=6'
sam_url = 'https://www.demoblaze.com/prod.html?idp_=1'
cart_ul = 'https://www.demoblaze.com/cart.html'


def setUp():
    print(f'Launch {app} App')
    print("\n")
    driver.maximize_window()
    driver.implicitly_wait(0.25)
    driver.get(demo_url)

    if driver.current_url == demo_url and driver.title == demo_home_page_title:
        print(f'Hello! {app} website launched successfully!\n')
        print(f'{app} Homepage URL: {driver.current_url}, Homepage title: {driver.title}')
        print("\n")
        sleep(0.25)
    else:
        print(f'{app} did not launch. Check your code or application.')
        print(f'Current URL: {driver.current_url}, Page title: {driver.title}')
        tearDown()

def tearDown():
    if driver is not None:
        print("\n")
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(0.28)
        driver.close()
        driver.quit()


def navigate():
    if driver.current_url == demo_url and driver.title == demo_home_page_title:
        driver.find_element(By.LINK_TEXT, 'Nexus 6').click()
        sleep(0.25)
        if driver.current_url == demo_nexus_dashboard_url:
            assert driver.current_url == demo_nexus_dashboard_url
            assert driver.title == demo_home_page_title
            print(f' ---- Search is successful. {app1} Dashboard is displayed - Page title: {driver.title}\n')
        else:
            print(f'Dashboard is not displayed. Check your code or website and try again.\n')
            #item 1
        driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div[2]/div/a').click()
        sleep(0.25)
        driver.switch_to.alert.accept()
        print('---Item 1 added. Proceed to Home page.---\n')
        driver.find_element(By.LINK_TEXT, 'PRODUCT STORE').click()
        sleep(0.28)
        print('Home Page displayed.\n')
        # Add item 2 to cart
        driver.find_element(By.LINK_TEXT, 'Sony xperia z5').click()
        sleep(0.25)
        if driver.current_url == sony_url:
            assert driver.current_url == sony_url
            assert driver.title == demo_home_page_title
            print(f' ---- Search is successful. Sony xperia z5 dashboard is displayed - Page title: {driver.title}\n')
        else:
            print(f'Dashboard is not displayed. Check your code or website and try again.\n')
        driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div[2]/div/a').click()
        sleep(0.25)
        driver.switch_to.alert.accept()
        print('---Item 2 added. Proceed to Homepage---\n')
        driver.find_element(By.LINK_TEXT, 'PRODUCT STORE').click()
        sleep(0.25)
        print('Home Page displayed.\n')
        # Add  item 3 to Cart
        driver.find_element(By.LINK_TEXT, 'Samsung galaxy s6').click()
        sleep(0.25)
        if driver.current_url == sam_url:
            assert driver.current_url == sam_url
            assert driver.title == demo_home_page_title
            print(f' ---- Search is successful. Samsung galaxy s6 dashboard is displayed - Page title: {driver.title}\n')
        else:
            print(f'Dashboard is not displayed. Check your code or website and try again.\n')
        driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div[2]/div/a').click()
        sleep(0.25)
        driver.switch_to.alert.accept()
        print('---Item 3 added. Proceed to Cart page---\n')

def cart():
    driver.find_element(By.LINK_TEXT, 'Cart').click()
    sleep(0.25)
    if driver.current_url == cart_ul:
        driver.find_element(By.XPATH, f'//td[contains(., inm)]').is_displayed()
        for i in range(len(item_list)):
             val = item_list[i], item_list[i], item_list[i]
        print(f'{val} Successfully in cart. {datetime.datetime.now()}\n')
    else:
        print(f'Dashboard is not displayed/ Item not it cart. Check your code or website and try again.\n')
    driver.find_element(By.LINK_TEXT, 'Delete').click()
    print('Sony xperia z5 successfully deleted from cart')
    sleep(2)


setUp()
navigate()
cart()
tearDown()