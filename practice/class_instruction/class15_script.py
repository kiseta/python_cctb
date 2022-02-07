from time import sleep

from selenium import webdriver

driver = webdriver.Chrome('../chromedriver')

# Make a full screen
driver.maximize_window()

# Let's wait for the browser response in general
driver.implicitly_wait(30)

# Navigating to the Moodle app website
driver.get('http://52.39.5.126')

# Checking that we're on the correct URL address and we're seeing correct title
if driver.current_url == 'http://52.39.5.126/' and driver.title == 'Software Quality Assurance Testing':
    print(f'We\'re at Moodle homepage -- {driver.current_url}')
    print(f'We\'re seeing title message -- "Software Quality Assurance Testing"')
    sleep(5)
    driver.close()
    driver.quit()
else:
    print(f'We\'re not at the Moodle homepage. Check your code!')
    driver.close()
    driver.quit()
