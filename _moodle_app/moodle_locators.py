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
first_name = fake.first_name()
last_name = fake.last_name()
middle_name = fake.first_name()

new_username = f'{first_name}{last_name}'.lower()
new_password = fake.password()
email = f'{new_username}@{fake.free_email_domain()}' #fake.email()
moodle_net_profile = f'https://moodle.net/{new_username}'
city = fake.city()
country = fake.current_country()
description = fake.sentence(nb_words = 75, variable_nb_words = True)
pic_desc = f'image submitted by {first_name} {last_name}'
list_of_interests = [fake.job(), fake.job(), fake.job(), fake.job()]
address = f'{fake.street_address()} {city} {fake.province_abbr()} {fake.postalcode()} {country}'
idnumber  = fake.bothify(text='????-#####', letters='QZXWOAY')
username1 = first_name.lower() + fake.bothify(text='###')
username2 = last_name.lower() + fake.bothify(text='###')
username3 = country.lower()+ fake.bothify(text='##') + first_name.lower()

lst_opt = ['Web page', 'ICQ number', 'Skype ID', 'AIM ID', 'Yahoo ID', 'MSN ID',
           'ID number', 'Institution', 'Department',
           'Phone', 'Mobile phone', 'Address']

lst_ids = ['id_url', 'id_icq', 'id_skype', 'id_aim', 'id_yahoo', 'id_msn',
           'id_idnumber', 'id_institution', 'id_department',
           'id_phone1', 'id_phone2', 'id_address']

lst_val = [fake.url(), username1, new_username, username2, new_username, username3,
           idnumber, fake.company(), fake.catch_phrase(),
           fake.phone_number(),fake.phone_number(), address]

print(lst_val)