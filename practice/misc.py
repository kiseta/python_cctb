from time import sleep
# create a ticking timer
seconds = 10
while seconds != 0:
    print(f'Time to self-destruct: {seconds}')
    # if input('Abort? Yes/No : ').capitalize() == 'Yes':
    #     break
    #     print(f'Self-destruct aborted at {seconds}')

    seconds = seconds - 1
    # seconds -=1
    sleep(1) # requires import: add to top of the file: from time import sleep

print(f'BOOM!🌟')