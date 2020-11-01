import time
import pyautogui

with open("shakespeare.txt", "r", encoding="utf8") as file:
    shakespeare = file.read()

##print(shakespeare[0:10000])

print(len(shakespeare))
time.sleep(3)
##pyautogui.typewrite(shakespeare[100000:101000])

block = 50
for i in range(0, len(shakespeare), block):
##    print("hi")
##    time.sleep(1)
    pyautogui.typewrite(shakespeare[i:i+block])
