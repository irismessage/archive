from random import choice
from time import sleep

def Stutter(Text):
    for i in range (len(Text)):
        print(Text[i], end='')
        sleep(choice([0.01, 0.02, 0.03, 0.04, 0.05]))
    print('')

while True:
    String = input()
    if String == 'end test':
        break
    else:
        Stutter(String)
        
