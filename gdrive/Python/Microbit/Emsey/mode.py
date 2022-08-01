from microbit import *

Modes = ['test()', 'sing()', 'rainbow()']


def sing():
    display.scroll('LA LA LA')


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


while True:
    setmode()
