from faker import Faker

# introduce Faker object to the file
# set localization to use only data related to Canada
fake = Faker(locale='en_CA')


# ------------------ MOODLE WEB ELEMENTS ------------------------------
app = 'Moodle LMS'
moodle_url = 'http://52.39.5.126/'
moodle_home_page_title = 'Software Quality Assurance Testing'
moodle_login_page_url = 'http://52.39.5.126/login/index.php'
moodle_login_page_title = 'Software Quality Assurance Testing: Log in to the site'
moodle_dashboard_url = 'http://52.39.5.126/my/'
moodle_dashboard_title = 'Dashboard'
moodle_username = 'tkuser'
moodle_password = 'Moodle!123'
# -------------------------------------------------

# generate fake data values for new user
new_username = fake.user_name()
new_password = fake.password()
first_name = fake.first_name()
last_name = fake.last_name()
email = fake.email()