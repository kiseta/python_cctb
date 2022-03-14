from faker import Faker
fake = Faker(locale=['en_CA', 'en_US'])
import random

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

# instock_inventory = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
#                      14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
#                      24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
# instock_inventory = [i for i in range(1, 35) if i != 13]
# product_id = random.choice(instock_inventory)
product_id = random.choice([x for x in range(1, 35) if x != 13])


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