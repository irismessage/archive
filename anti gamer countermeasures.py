import math
import time

import ctypes

import pyperclip
import pynput

##import pyautogui
##pyautogui.typewrite("test")

##max_message_length = 510
max_message_length = 500
# min time between messages: exactly 1 second.
# hence delay in code set to 1.1 seconds


print("Press enter to start.")
input()
print("Starting in 2 seconds.")
# Time delay to let you select the textbox.
time.sleep(2)

def h(word, cut=0):
    l = len(word)
    print(l)
    print(max_message_length / l)
    count = math.floor(max_message_length / l)
    print(count)
    print(l * count)
    print("Cut value " + str(cut))
    print(count - cut)
    print(l * (count-cut))
    print(word * (count-cut))


    # 29 is the maximum for some flags
    # set to maths value for max message length or 29 for even distribution
    count = 29
    print("Count value used: " + str(count))
    copies = count - cut
    print("Copies value used: " + str(copies))

    messages.append(word * copies)

def generate_messages(cut=0):
    global messages
    messages = []

    with open("twitch spam text.txt", "r") as words_file:
        for line in words_file:
            line = line.replace("\n", "")
            h(line, cut)
            print("")

##        print(messages)



ENTER = 0x1C
LEFT_CONTROL = 0x1D
V = 0x2F

SendInput = ctypes.windll.user32.SendInput

# Presses and permanently holds down a keyboard key
def PressKeyPynput(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = pynput._util.win32.INPUT_union()
    ii_.ki = pynput._util.win32.KEYBDINPUT(0, hexKeyCode, 0x0008, 0, ctypes.cast(ctypes.pointer(extra), ctypes.c_void_p))
    x = pynput._util.win32.INPUT(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

# Releases a keyboard key if it is currently pressed down
def ReleaseKeyPynput(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = pynput._util.win32.INPUT_union()
    ii_.ki = pynput._util.win32.KEYBDINPUT(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.cast(ctypes.pointer(extra), ctypes.c_void_p))
    x = pynput._util.win32.INPUT(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def output_to_textbox():
    for message in messages:
    ##    pyautogui.typewrite(message)
        pyperclip.copy(message)
        PressKeyPynput(LEFT_CONTROL)
        PressKeyPynput(V)
        ReleaseKeyPynput(LEFT_CONTROL)
        ReleaseKeyPynput(V)
        
        PressKeyPynput(ENTER)
        ReleaseKeyPynput(ENTER)

##        time.sleep(1.1)
        time.sleep(1.25)

for i in range(0,4,1):
    generate_messages(cut=i)

    output_to_textbox()
    

##print("30 second delay")
##time.sleep(30)
##print("30 second delay over")
