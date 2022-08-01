# Add your Python code here. E.g.
from microbit import *
import radio

blink = Image("99999:"
              "99999:"
              "99999:"
              "99999:"
              "99999")
radio.on()
while True:
    if button_a.is_pressed():
        radio.send('ON')
        display.scroll('SENDING')
    incoming = radio.receive()
    if incoming == 'ON':
        for i in range (9):
            blink.fill(i)
            display.show(blink)
        for i in range (9, 0, -1):
            blink.fill(i)
            display.show(blink)
        sleep(5000)
    else:
        display.show(Image.NO)