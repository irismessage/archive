from microbit import *
from random import choice
import neopixel

# motors
MDirs = [0, 0]


def righton(Speed, Direction):
    MDirs[1] = Direction
    if Direction == 0:
        ASValue = (1023 / 100) * Speed
    else:
        ASValue = 1023 - ((1023 / 100) * Speed)
    pin1.write_analog(ASValue)
    pin12.write_digital(Direction)


def rightoff():
    if MDirs[1] == 0:
        pin1.write_analog(0)
    else:
        pin1.write_analog(1023)


def lefton(Speed, Direction):
    MDirs[0] = Direction
    if Direction == 0:
        ASValue = (1023 / 100) * Speed
    else:
        ASValue = 1023 - ((1023 / 100) * Speed)
    pin0.write_analog(ASValue)
    pin8.write_digital(Direction)


def leftoff():
    if MDirs[0] == 0:
        pin0.write_analog(0)
    else:
        pin0.write_analog(1023)


def allon(Speed, Direction):
    lefton(Speed, Direction)
    righton(Speed, Direction)


def alloff():
    leftoff()
    rightoff()

# turn


def turn(Directionlr, SpeedN, Ratio):
    if Directionlr == 'l':
        RASValue = SpeedN
        RDDValue = 0
        LASValue = (RASValue / 100) * Ratio
        LDDValue = 1
    elif Directionlr == 'r':
        LASValue = SpeedN
        LDDValue = 0
        RASValue = (LASValue / 100) * Ratio
        RDDValue = 1
    righton(RASValue, RDDValue)
    lefton(LASValue, LDDValue)


def turnfor(Degrees):
    Heading = compass.heading()
    Target = Heading + Degrees
    if Degrees < 0:
        turn('l', 50, 100)
    elif Degrees > 0:
        turn('r', 50, 100)
    while True:
        Heading = compass.heading()
        if Heading > Target - 5 and Heading < Target + 5:
            alloff()
            break

# neopixels


def leftpixel(PixelIndx, Red, Green, Blue):
    Pixels = neopixel.NeoPixel(pin13, 12)
    Pixels[PixelIndx] = (Red, Green, Blue)
    Pixels.show()


def rightpixel(PixelIndx, Red, Green, Blue):
    Pixels = neopixel.NeoPixel(pin13, 12)
    Pixels[PixelIndx + 5] = (Red, Green, Blue)
    Pixels.show()


def allpixels(Red, Green, Blue):
    Pixels = neopixel.NeoPixel(pin13, 12)
    for i in range(len(Pixels)):
        Pixels[i] = (Red, Green, Blue)
    Pixels.show()

# buzzer


def buzzon():
    pin14.write_digital(1)


def buzzoff():
    pin14.write_digital(0)


def buzz(Time):
    buzzon()
    sleep(Time * 1000)
    buzzoff()

# sensors


def light(Select):
    pin16.write_digital(Select)
    Reading = pin2.read_analog()
    Percentage = (Reading / 1023) * 100
    Rounded = round(Percentage)
    return Rounded


def line(Select):
    if Select == 0:
        return pin11.read_digital()
    else:
        return pin5.read_digital()


# quotes
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


def quote():
    Saying = choice(Quotes)
    display.scroll(Saying, delay=75, wait=False, monospace=True)
    Used.append(Saying)
    del Quotes[Quotes.index(Saying)]
    if len(Quotes) == 0:
        for i in range(len(Used)):
            Quotes.append(Used.pop())


# modes
Modes = ['test()', 'dostuff()']


def setmode():
    display.scroll('SET MODE', delay=75)
    Mode = ''
    for i in range(4):
        while True:
            if button_a.is_pressed() or button_b.is_pressed():
                break
        if button_a.is_pressed():
            Mode = Mode + '0'
        elif button_b.is_pressed():
            Mode = Mode + '1'
        display.scroll(str(Mode), delay=75)
    IntMode = int(Mode, 2)
    display.scroll(str(IntMode))
    try:
        SubMode = Modes[IntMode]
        eval(SubMode)
    except:
        display.scroll('NO MODE AT ' + str(IntMode), delay=75)
