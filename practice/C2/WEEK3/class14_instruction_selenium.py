from time import sleep

from selenium import webdriver  # import selenium to the file

# create a Chrome driver instance, specify path to chromedriver file
driver = webdriver.Chrome('../../../chromedriver.exe')

# Make browser full screen
driver.maximize_window()

# Give browser up to 30 seconds to respond
driver.implicitly_wait(30)

# Navigate to Moodle app website
driver.get('http://52.39.5.126/')

# Check that Moodle URL and the home page title are displayed
if driver.current_url == 'http://52.39.5.126/' and driver.title == 'Software Quality Assurance Testing':
    print('Yey! Moodle Launched Successfully')
    print(f'Moodle homepage URL: {driver.current_url}, Home Page Title: {driver.title}')
    sleep(5)
    driver.close()
else:
    print(f'Mooodle did not launch. Check your code or application!')
    print(f'Current URL: {driver.current_url}, Page Title: {driver.title}')
    driver.close()
    driver.quit()
