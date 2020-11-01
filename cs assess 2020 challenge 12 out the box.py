import pyautogui

# Pixel co-ords of buttons when fullscreen with start of grey box
# straight under bookmarks bar.
keypad_keys = {"1": (820, 420),
               "2": (950, 430),
               "3": (1080, 430),
               "4": (820, 550),
               "6": (1080, 550),
               "7": (820, 680),
               "8": (950, 680),
               "9": (1080, 680),
               "0": (950, 800)}

code = "3986298476438073"


# Focus window.
pyautogui.click(1000, 1000)

# Input code.
for digit in code:
    key_coords = keypad_keys[digit] 
    pyautogui.click(key_coords[0], key_coords[1])


# Loop to get locations of keys.
##while True:
##    print(pyautogui.position())
