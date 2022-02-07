from time import sleep

from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')

# Make browser full screen
driver.maximize_window()

# Give the browser up to 30 seconds to respond
driver.implicitly_wait(30)

# Navigate to Moodle app website
driver.get('http://52.39.5.126')

# Check Moodle URL and the home page title are displayed
if driver.current_url == 'http://52.39.5.126/' and driver.title == 'Software Quality Assurance Testing':
    print(f'Yey! Moodle launched successfully!')
    print(f'Moodle homepage URL: {driver.current_url}')
    print(f'Home page title: {driver.title}')
    sleep(5)
    driver.close()
else:
    print(f'Moodle did not launch. Check your code or the application')
    print(f'Current URL: {driver.current_url}')
    print(f'Home page title: {driver.title}')
    driver.close()
    driver.quit()
