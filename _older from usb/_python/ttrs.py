from win32api import *
from win32con import *

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

NumCoords = {'1': [,], '2': [,], '3': [,], '4': [,], '5': [,],
             '6': [,], '7': [,], '8': [,], '9': [,], '0': [,],}

def enter(Num):
    Num = str(Num)
    for i in range(len(Num)):
        click(NumCoords[Num[i]])
    click(X, X)
