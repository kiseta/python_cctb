from faker import Faker

# introduce Faker object to the file
# set localization to use only data related to Canada
fake = Faker(locale='en_CA')


# ------------------ MOODLE WEB ELEMENTS ------------------------------
app = 'Moodle LMS'
moodle_username = 'tkuser'
moodle_password = 'Moodle!123'
moodle_url = 'http://52.39.5.126/'
moodle_home_page_title = 'Software Quality Assurance Testing'
moodle_login_page_url = 'http://52.39.5.126/login/index.php'
moodle_login_page_title = 'Software Quality Assurance Testing: Log in to the site'
moodle_dashboard_url = 'http://52.39.5.126/my/'
moodle_dashboard_title = 'Dashboard'
moodle_users_main_page = 'http://52.39.5.126/admin/user.php'
moodle_users_main_page_title ='SQA: Administration: Users: Accounts: Browse list of users'
# -------------------------------------------------

# generate fake data values for new user
first_name = fake.first_name()
last_name = fake.last_name()
middle_name = fake.first_name()
full_name = f'{first_name} {last_name}'
# new_username = fake.user_name()
new_username = f'{first_name}{last_name}'.lower()
new_password = fake.password()
email = f'{new_username}@{fake.free_email_domain()}' #fake.email()
#print(email)
moodle_net_profile = f'https://moodle.net/{new_username}'
city = fake.city()
country = fake.current_country()
description = f'User added by {moodle_username} via Selenium Python Automation Framework' # fake.sentence(nb_words = 75, variable_nb_words = True)
pic_desc = f'image submitted by {first_name} {last_name}'
list_of_interests = [fake.job(),fake.job(),fake.job(),fake.job()]
address = f'{fake.street_address()} {city} {fake.province_abbr()} {fake.postalcode()} {country}'
address1 = fake.address().replace("\n", " ")
idnumber  = fake.bothify(text='????-#####', letters='QZXWOAY')
icq_num = fake.pyint(111111,999999)
id_aim = last_name.lower() + str(fake.pyint(11,999999))
id_msn = first_name.lower() + str(fake.pyint(11,99)) + country.lower()

lst_opt = ['Web page', 'ICQ number', 'Skype ID', 'AIM ID', 'Yahoo ID', 'MSN ID',
           'ID number', 'Institution', 'Department',
           'Phone', 'Mobile phone', 'Address']

lst_ids = ['id_url', 'id_icq', 'id_skype', 'id_aim', 'id_yahoo', 'id_msn',
           'id_idnumber', 'id_institution', 'id_department',
           'id_phone1', 'id_phone2', 'id_address']

lst_val = [fake.url(), icq_num, new_username, id_aim, new_username, id_msn,
           idnumber, fake.company(), fake.catch_phrase(),
           fake.phone_number(),fake.bothify(text='1-(###)-###-####'), address1]

#print(lst_val)