from faker import Faker
fake = Faker(locale=['en_CA', 'en_US'])

# ------------------ AOS WEB ELEMENTS ------------------------------
app = 'Advantage Online Shopping'
base_url = 'https://advantageonlineshopping.com/#/'
#base_url = 'http://localhost:8080/#/'
new_account_url = base_url + 'register'
new_account_page_title = 'CREATE NEW ACCOUNT'
home_page_title = '\xa0Advantage Shopping'

first_name = fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'
user_name = f'{first_name}{last_name}'.lower()[:12]
password = 'Pass1'
user_email = f'{user_name}@{fake.free_email_domain()}'
phone = fake.bothify(text='1-(###)-###-####')
country = 'Canada'
city = fake.city()[:10]
address = fake.street_address()
province = fake.province_abbr()
postal_code = fake.postalcode()
product_name = ''
#pname = " ".join(w.capitalize() for w in product_name.split())
order_number = ''
tracking_number = ''
categories = ['SPEAKERS','TABLETS','LAPTOPS','MICE','HEADPHONES']


hr = f'\n------------------------~*~--------------------------'

list_name = ['usernameRegisterPage', 'emailRegisterPage', 'passwordRegisterPage', 'confirm_passwordRegisterPage',
             'first_nameRegisterPage', 'last_nameRegisterPage', 'phone_numberRegisterPage',
             'cityRegisterPage', 'addressRegisterPage', 'state_/_province_/_regionRegisterPage',
             'postal_codeRegisterPage']

list_val = [user_name, user_email, password, password,
            first_name, last_name, phone,
            city, address, province, postal_code]

print(list_val)


# -------------------------------------------------