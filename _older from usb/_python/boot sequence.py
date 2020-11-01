from time import sleep
from random import randint

#boot sequence

def loading_bar():
    for i in range(25-1):
        print('█', end='')
        sleep(randint(1, 10)/100)
    print('█ \n')

if input('START BOOT SEQUENCE? Y/N \n').upper() == 'Y':
    print('LOADING...')
    loading_bar()
    print('PUTTING ON SOCKS...')
    loading_bar()
    print('PUTTING FOOT IN BOOT...')
    loading_bar()
    print('DOING UP LACES...')
    loading_bar()
    print('BOOT SEQUENCE COMPLETE')
else:
    pass
