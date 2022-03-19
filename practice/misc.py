from time import sleep
from faker import Faker
fake = Faker(locale='en_CA')

s = 'http://52.39.5.126/user/view.php?id=8769&course=1'
start = '='
end = '&'
print(s.find(start))
print(s.rfind(end))
print(s[s.find(start) + len(start) : s.rfind('&')])

def find_between_r(val, first):
    try:
        start = val.find(first) + len(first)
        end = len(val)
        return val[start:end]
    except ValueError:
        return ""

print(find_between_r('http://52.39.5.126/user/view.php?id=5363','='))

# find() will return the index of the first match. But
# rfind() will give you the last occurence of the pattern
h = 'http://52.39.5.126/user/view.php?id=543543'
print(h[h.find('=') + 1 : len(h)])

dh = 'http://52.39.5.126/admin/user.php?sort=name&dir=ASC&perpage=30&page=0&delete=1356&sesskey=EPuIOUEm0h'
print(dh[dh.find('delete=') + len('delete=') : dh.rfind('&')])
start = dh.find('delete=') + len('delete=')
end = dh.rfind('&')
print(dh[start : end])

email = fake.email()
print(email)
address = fake.address()#.replace('\n', " ")
print(address)


# # create a ticking timer
# seconds = 10
# while seconds != 0:
#     print(f'Time to self-destruct: {seconds}')
#     if input('Abort? Yes/No : ').capitalize() == 'Yes':
#         print(f'Self-destruct aborted at {seconds}')
#         break
#
#     seconds = seconds - 1
#     # seconds -=1
#     sleep(1) # requires import: add to top of the file: from time import sleep
#     print(f'BOOM!🌟')


fullname = "Edwrd Cullen"
fullname_check = 'Welcome Edward Cullen'

print("pass ✅" if fullname in fullname_check else "fail ✖")