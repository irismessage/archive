from time import sleep
print('Welcome to CCC!')
print( )

while True:
    print('First, enter your earn rate.')
    CPS = input()
    print('Now, enter the price of what you want to buy.')
    Price = input()
    print('Finally, enter the current cookies you have.')
    Owned = input()

    Required = int(Price) - int(Owned)
    Seconds = int(Required) / int(CPS)
    Minutes = int(Seconds) / 60
    TimeLeft = Minutes
    
    if Minutes < 0:
        print('You can buy what you want now.')
    else:
        print('You can buy what you want in', int(Minutes), 'minutes.')
        while TimeLeft > 0:
            sleep(60)
            TimeLeft = int(TimeLeft) - 1
            if TimeLeft <= 0:
                print('You can buy it now!')
            else:
                print(TimeLeft, 'minutes...')

    print( )


