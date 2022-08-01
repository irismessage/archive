from microbit import *
from random import choice
import neopixel

display.scroll('starting')

class bitbot:
    # init bruv
    def __init__(self, Modes, Quotes, Used, MDirs):
        self.Modes = Modes
        self.Quotes = Quotes
        self.Used = Used
        self.MDirs = MDirs

    # motors
    def righton(self, Speed, Direction):
        self.MDirs[1] = Direction
        if Direction == 0:
            ASValue = (1023 / 100) * Speed
        else:
            ASValue = 1023 - ((1023 / 100) * Speed)
        pin1.write_analog(ASValue)
        pin12.write_digital(Direction)

    def rightoff(self):
        if self.MDirs[1] == 0:
            pin1.write_analog(0)
        else:
            pin1.write_analog(1023)

    def lefton(self, Speed, Direction):
        self.MDirs[0] = Direction
        if Direction == 0:
            ASValue = (1023 / 100) * Speed
        else:
            ASValue = 1023 - ((1023 / 100) * Speed)
        pin0.write_analog(ASValue)
        pin8.write_digital(Direction)

    def leftoff(self):
        if self.MDirs[0] == 0:
            pin0.write_analog(0)
        else:
            pin0.write_analog(1023)

    def allon(self, Speed, Direction):
        self.lefton(Speed, Direction)
        self.righton(Speed, Direction)

    def alloff(self):
        self.leftoff()
        self.rightoff()

    # turn
    def turn(self, Directionlr, SpeedN, Ratio):
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
        self.righton(RASValue, RDDValue)
        self.lefton(LASValue, LDDValue)

    def turnfor(self, Degrees):
        Heading = compass.heading()
        Target = Heading + Degrees
        if Degrees < 0:
            self.turn('l', 50, 100)
        elif Degrees > 0:
            self.turn('r', 50, 100)
        while True:
            Heading = compass.heading()
            if Heading > Target - 5 and Heading < Target + 5:
                self.alloff()
                break

    # neopixels
    def leftpixel(self, PixelIndx, Red, Green, Blue):
        Pixels = neopixel.NeoPixel(pin13, 12)
        Pixels[PixelIndx] = (Red, Green, Blue)
        Pixels.show()

    def rightpixel(self, PixelIndx, Red, Green, Blue):
        Pixels = neopixel.NeoPixel(pin13, 12)
        Pixels[PixelIndx + 5] = (Red, Green, Blue)
        Pixels.show()

    def allpixels(self, Red, Green, Blue):
        Pixels = neopixel.NeoPixel(pin13, 12)
        for i in range(len(Pixels)):
            Pixels[i] = (Red, Green, Blue)
        Pixels.show()

    # buzzer
    def buzzon(self):
        pin14.write_digital(1)

    def buzzoff(self):
        pin14.write_digital(0)

    def buzz(self, Time):
        pin14.write_digital(1)
        sleep(Time * 1000)
        pin14.write_digital(0)

    # sensors
    #def light(self, Select):
     #   pin16.write_digital(Select)
      #  Reading = pin2.read_analog()
       # Percentage = (Reading / 1023) * 100
       # Rounded = round(Percentage)
       # return Rounded

    #def line(self, Select):
     #   if Select == 0:
      #      return pin11.read_digital()
      #  else:
       #     return pin5.read_digital()

    # quotes
    def quote(self):
        Saying = choice(Quotes)
        display.scroll(Saying, delay=75, wait=False, monospace=True)
        Used.append(Saying)
        del Quotes[Quotes.index(Saying)]
        if len(Quotes) == 0:
            for i in range(len(Used)):
                Quotes.append(Used.pop())

    # modes
    def setmode(self):
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
            SubMode = self.Modes[IntMode]
            eval(SubMode)
        except:
            display.scroll('NO MODE AT ' + str(IntMode), delay=75)

    def test(self):
        display.scroll('Testing...', delay=75, wait=False)
        self.righton(50, 0)
        sleep(500)
        self.rightoff()
        self.righton(50, 1)
        sleep(500)
        self.rightoff()
        self.lefton(50, 0)
        sleep(500)
        self.leftoff()
        self.lefton(50, 1)
        sleep(500)
        self.rightoff()
        self.allon(50, 0)
        sleep(500)
        self.alloff()
        self.allon(50, 1)
        sleep(500)
        self.alloff()
        display.scroll('Test complete.', delay=75)


# test
display.scroll('0', delay=75)
Modes = ['self.test()', 'self.dostuff()']
display.scroll('1', delay=75)
Quotes = list()
display.scroll('2', delay=75)
Used = list()
display.scroll('3', delay=75)
MDirs = [0, 0]
display.scroll('4', delay=75)
robot = bitbot(Modes, Quotes, Used, MDirs)
display.scroll('5', delay=75)

while True:
    display.scroll('Running...', delay=75)
    robot.setmode()
