from microbit import *
display.show(Image.DIAMOND)

import neopixel
import math

Pixels = neopixel.NeoPixel(pin13, 12)

def leftpixel(PixelIndx, Red, Green, Blue):
    Pixels[PixelIndx] = (Red, Green, Blue)
    Pixels.show()

def rightpixel(PixelIndx, Red, Green, Blue):
    Pixels[PixelIndx + 6] = (Red, Green, Blue)
    Pixels.show()

def allpixels(Red, Green, Blue):
    for i in range(len(Pixels)):
        Pixels[i] = (Red, Green, Blue)
        Pixels.show()

def forward(Red, Green, Blue, Delay):
    leftpixel(0, Red, Green, Blue)
    rightpixel(0, Red, Green, Blue)
    sleep(Delay)
    for i in range(5):
        leftpixel(i + 1, Red, Green, Blue)
        rightpixel(i + 1, Red, Green, Blue)
        leftpixel(i, 0, 0, 0)
        rightpixel(i, 0, 0, 0)
        sleep(Delay)
    leftpixel(5, 0, 0, 0)
    rightpixel(5, 0, 0, 0)
    sleep(Delay + 100)
    
def leftforward(Red, Green, Blue, Delay):
    leftpixel(0, Red, Green, Blue)
    sleep(Delay)
    for i in range(5):
        leftpixel(i + 1, Red, Green, Blue)
        leftpixel(i, 0, 0, 0)
        sleep(Delay)
    leftpixel(5, 0, 0, 0)
    sleep(Delay + 100)

def rightforward(Red, Green, Blue, Delay):
    rightpixel(0, Red, Green, Blue)
    sleep(Delay)
    for i in range(5):
        rightpixel(i + 1, Red, Green, Blue)
        rightpixel(i, 0, 0, 0)
        sleep(Delay)
    rightpixel(5, 0, 0, 0)
    sleep(Delay + 100)

def back(Red, Green, Blue, Delay):
    leftpixel(5, Red, Green, Blue)
    rightpixel(5, Red, Green, Blue)
    sleep(Delay)
    for i in range(5, 0, -1):
        leftpixel(i - 1, Red, Green, Blue)
        rightpixel(i - 1, Red, Green, Blue)
        leftpixel(i, 0, 0, 0)
        rightpixel(i, 0, 0, 0)
        sleep(Delay)
    leftpixel(0, 0, 0, 0)
    rightpixel(0, 0, 0, 0)
    sleep(Delay + 100)

def leftback(Red, Green, Blue, Delay):
    leftpixel(5, Red, Green, Blue)
    sleep(Delay)
    for i in range(5, 0, -1):
        leftpixel(i - 1, Red, Green, Blue)
        leftpixel(i, 0, 0, 0)
        sleep(Delay)
    leftpixel(0, 0, 0, 0)
    sleep(Delay + 100)

def rightback(Red, Green, Blue, Delay):
    rightpixel(5, Red, Green, Blue)
    sleep(Delay)
    for i in range(5, 0, -1):
        rightpixel(i - 1, Red, Green, Blue)
        rightpixel(i, 0, 0, 0)
        sleep(Delay)
    rightpixel(0, 0, 0, 0)
    sleep(Delay + 100)

def rainbow():
    Frequency = 0.3
    for i in range(21):
        Red = (math.sin(Frequency * i + 0) * 127 + 128) / 10
        Green = (math.sin(Frequency * i + 2) * 127 + 128) / 10
        Blue = (math.sin(Frequency * i + 4) * 127 + 128) / 10
        allpixels(int(Red), int(Green), int(Blue))
        sleep(100)


Red = 1
Green = 3
Blue = 10

Frequency = 0.3
while True:
    for i in range(3):
        Red = int((math.sin(Frequency * i + 0) * 127 + 128) / 10)
        Green = int((math.sin(Frequency * i + 2) * 127 + 128) / 10)
        Blue = int((math.sin(Frequency * i + 4) * 127 + 128) / 10)
        i += 1
        forward(Red, Green, Blue, 10)
        Red = int((math.sin(Frequency * i + 0) * 127 + 128) / 10)
        Green = int((math.sin(Frequency * i + 2) * 127 + 128) / 10)
        Blue = int((math.sin(Frequency * i + 4) * 127 + 128) / 10)
        i += 1
        leftforward(Red, Green, Blue, 10)
        Red = int((math.sin(Frequency * i + 0) * 127 + 128) / 10)
        Green = int((math.sin(Frequency * i + 2) * 127 + 128) / 10)
        Blue = int((math.sin(Frequency * i + 4) * 127 + 128) / 10)
        i += 1
        rightforward(Red, Green, Blue, 10)
        Red = int((math.sin(Frequency * i + 0) * 127 + 128) / 10)
        Green = int((math.sin(Frequency * i + 2) * 127 + 128) / 10)
        Blue = int((math.sin(Frequency * i + 4) * 127 + 128) / 10)
        i += 1
        back(Red, Green, Blue, 10)
        Red = int((math.sin(Frequency * i + 0) * 127 + 128) / 10)
        Green = int((math.sin(Frequency * i + 2) * 127 + 128) / 10)
        Blue = int((math.sin(Frequency * i + 4) * 127 + 128) / 10)
        i += 1
        leftback(Red, Green, Blue, 10)
        Red = int((math.sin(Frequency * i + 0) * 127 + 128) / 10)
        Green = int((math.sin(Frequency * i + 2) * 127 + 128) / 10)
        Blue = int((math.sin(Frequency * i + 4) * 127 + 128) / 10)
        i += 1
        rightback(Red, Green, Blue, 10)
        Red = int((math.sin(Frequency * i + 0) * 127 + 128) / 10)
        Green = int((math.sin(Frequency * i + 2) * 127 + 128) / 10)
        Blue = int((math.sin(Frequency * i + 4) * 127 + 128) / 10)
        i += 1
        forward(Red, Green, Blue, 10)
