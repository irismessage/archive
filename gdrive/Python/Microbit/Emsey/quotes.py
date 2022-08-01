from microbit import *
from random import choice

Quotes = list()
Quotes.append('EXTERMINATE')
Quotes.append('I\'m a bot, beep boop')
Quotes.append('Come with me if you want to live')
Quotes.append('Hey look, I\'m stealing your jobs')
Quotes.append('I think you ought to know I\'m feeling very depressed')
Quotes.append('Mere flesh is no match for real steel')
Quotes.append('Citizen, stand down')
Quotes.append('You have 20 seconds to comply')
Quotes.append('Beep bloop blop bleep boop')
Quotes.append('We\'re doomed')
Quotes.append('AIIIIIIEEEEE')
Quotes.append('Roger roger')
Quotes.append('Resistance is fultile')
Quotes.append('You will be assimilated')

Used = list()
while True:
    Saying = choice(Quotes)
    display.scroll(Saying, delay=75, monospace=True)
    Used.append(Saying)
    del Quotes[Quotes.index(Saying)]
    if len(Quotes) == 0:
        for i in range(len(Used)):
            Quotes.append(Used.pop())
    sleep(1000)
