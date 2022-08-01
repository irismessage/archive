from microbit import *
import neopixel

Pixels = neopixel.NeoPixel(pin13, 12)


def allpixels(Red, Green, Blue):
    for i in range(len(Pixels)):
        Pixels[i] = (Red, Green, Blue)
        Pixels.show()


def buzzon():
    pin14.write_digital(1)


def buzzoff():
    pin14.write_digital(0)


def buzz(Time):
    pin14.write_digital(1)
    sleep(Time)
    pin14.write_digital(0)


BuzzTimes = [200, 200, 400, 400, 400, 800, 200, 200, 400, 400, 400, 800, 200,
             200, 400, 400, 400, 400, 400, 200, 200, 400, 400, 400, 800]
SlepTimes = [100, 50,  100, 100, 100, 200, 100, 100, 100, 100, 100, 200, 100,
             50,  100, 100, 100, 100, 400, 100, 50,  100, 100, 100, 100]

Dir = 0
while True:
    for i in range(25):
        buzz(BuzzTimes[i])

        pin1.write_analog(511)
        pin12.write_digital(Dir)
        if Dir == 0:
            Dir = 1
            allpixels(0, 10, 0)
        else:
            Dir = 0
            allpixels(0, 0, 10)
        pin0.write_analog(511)
        pin8.write_digital(Dir)

        sleep(SlepTimes[i])
    pin0.write_analog(1023)
    pin1.write_analog(0)
    allpixels(0, 0, 0)
    sleep(3000)
