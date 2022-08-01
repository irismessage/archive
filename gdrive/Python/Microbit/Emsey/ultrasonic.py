from microbit import *


def ping():
    Timer = 0

    # start pulse
    pin15.set_analog_period_microseconds(10)
    pin15.write_analog(1023)

    # read echo length
    while True:
        if pin15.read_digital() == 1:
            break
    while pin15.read_digital() == 1:
        Timer += 1

    return Timer


while True:
    display.scroll('SENSING...', delay=50)
    Distance = ping()
    display.scroll(str(Distance))
