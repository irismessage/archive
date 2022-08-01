from microbit import *
import radio
radio.on()

Mode = 1
display.scroll('READY TO RECIEVE', delay=75)
while True:
    if accelerometer.is_gesture('left'):
        Mode = 1
        display.scroll('READY TO RECIEVE', delay=50)
    elif accelerometer.is_gesture('right'):
        Mode = 2

    if Mode == 1:
        Trigger = radio.receive()
        if Trigger == 'HEYLISTEN':
            Message = radio.receive
            display.scroll(str(Message))

    elif Mode == 2:
        Message = ''
        Loop = True
        while Loop is True:
            ASCII = 65
            while True:
                if accelerometer.is_gesture('down'):
                    display.scroll('DEVICE PRIMED', delay=50)
                    while True:
                        if not accelerometer.is_gesture('down'):
                            break
                    Loop = False
                    break
                if accelerometer.is_gesture('up'):
                    Message = str(Message) + chr(ASCII)
                    display.scroll(Message)
                    while True:
                        if not accelerometer.is_gesture('up'):
                            break
                    break
                elif button_a.is_pressed():
                    if ASCII > 64:
                        ASCII = ASCII - 1
                    while True:
                        if not button_a.is_pressed() and not button_b.is_pressed():
                            break
                elif button_b.is_pressed():
                    if ASCII < 123:
                        ASCII = ASCII + 1
                    while True:
                        if not button_a.is_pressed() and not button_b.is_pressed():
                            break
                display.show(chr(ASCII))
        display.scroll('SENDING...', delay=75)
        radio.send('HEYLISTEN')
        radio.send(Message)
        Loop = True
