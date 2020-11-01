from random import randint
print('Welcome to random number generator')
print('To start, pick a lowest number')
LowNum = input()
print('Now pick a highest number.')
HighNum = input()
print('Picking a random number...')
Number = randint(int(LowNum), int(HighNum))
print('Your random number is', Number)
while True:
    print('To repeat with the same numbers, press R.')
    print('To pick new numbers, press C')
    Option = input()
    if Option == 'r' or Option == 'R' or Option == 'c' or Option == 'C':
        ValidResponse = True
    else:
        ValidResponse = False
    while ValidResponse == False:
        print('That is not a valid response. Please try again.')
        Option = input()
        if Option == 'r' or Option == 'R' or Option == 'c' or Option == 'C':
            ValidResponse = True
    if Option == 'r' or Option == 'R':
        print('Picking a random number...')
        Number = randint(int(LowNum), int(HighNum))
        print('Your random number is', Number)
    if Option == 'c' or Option == 'C':
        print('Pick a lowest number')
        LowNum = input()
        print('Now pick a highest number.')
        HighNum = input()
        print('Picking a random number...')
        Number = randint(int(LowNum), int(HighNum))
        print('Your random number is', Number)
        

        
