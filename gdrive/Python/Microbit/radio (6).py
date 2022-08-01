# Add your Python code here. E.g.
from microbit import *
import radio

radio.on()
while True:
    if button_a.is_pressed():
        radio.send('ON')
        display.scroll('SENDING')
    incoming = radio.receive()
    if incoming == 'ON':
        display.show(Image.YES)
        sleep(5000)
    else:
        display.show(Image.NO)