from random import randint
from time import sleep

#test
##line = ''
##for i in range(80):
##    line += 'l'
##for i in range(40):
##    print(line)

def new_line(width, difficulty):
    line = ['l']
    for i in range(width-2):
        if randint(1, 70) <= difficulty:
            line.append('B')
        else:
            line.append(' ')
    line.append('l')

    return line

for i in range(40):
    print(''.join(new_line(80, 1)))
while True:
    print(''.join(new_line(80, 1)))
    sleep(0.1)
