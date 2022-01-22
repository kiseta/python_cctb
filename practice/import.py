__author__ = 'tk'
import time
from time import sleep, asctime

current_date = time.asctime()
print('~*~*~*~*~*~*~*~*~*~*~*~')
print(f'Test started {current_date}')

seconds = 10
while seconds != 0:
    print(seconds)
    seconds -=1
    sleep(1)
