# Add your Python code here. E.g.
from microbit import *


while True:
    if button_a.is_pressed():
        pin0.write_digital(1)
        display.scroll('SENDING')
    else:
        pin0.write_digital(0)
    Input = pin1.read_digital()
    if Input == 1:
        display.show(Image.YES)
    else:
        display.show(Image.NO)
