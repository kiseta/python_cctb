from faker import Faker

fake = Faker(locale="en_CA")

opencart_url = "https://www.opencart.com/"
register_url = "https://www.opencart.com/index.php?route=account/register"
marketplace_url = "https://www.opencart.com/index.php?route=marketplace/extension"
contact_us_url = "https://www.opencart.com/index.php?route=support/contact"
homepage_url = "https://www.opencart.com/index.php?route=common/home"
new_username = fake.user_name()
first_name = fake.first_name()
last_name = fake.last_name()
email = fake.email()
new_password = fake.password()
PIN_number = fake.pyint(1111, 9999)