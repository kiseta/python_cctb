from faker import Faker
fake = Faker(locale='en_CA')

#------------------ locators section-------------------------------
app = 'Moodle'
admin_username = 'tkuser'
admin_password = 'Moodle!123'
moodle_url = 'http://52.39.5.126/'
moodle_home_page_title = 'Software Quality Assurance Testing'
moodle_login_page_url = 'http://52.39.5.126/login/index.php'
moodle_login_page_title = 'Software Quality Assurance Testing: Log in to the site'
moodle_dashboard_url = 'http://52.39.5.126/my/'
moodle_dashboard_page_title = 'Dashboard'
moodle_add_new_user_page_title = 'SQA: Administration: Users: Accounts: Add a new user'

# -------------------- data section ---------------------------------
first_name = fake.first_name()
last_name = fake.last_name()
middle_name = fake.first_name()
full_name = f'{first_name} {last_name}'

new_username = f'{first_name}{last_name}'.lower()
new_password = fake.password()
email = f'{new_username}@{fake.free_email_domain()}'
email1 = fake.email()

moodle_net_profile = f'https://moodle.net/{new_username}'
city = fake.city()
country = fake.current_country()
description = f'User added by {admin_username} via Python Selenium Automated Script' #fake.sentence(nb_words=100) #

pic_desc = f'pic submited by {full_name}'

print(first_name, last_name, middle_name, new_username, new_password, email, email1)