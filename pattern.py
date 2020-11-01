from tkinter import *
from time import sleep
from random import randint

def hex(RGB):
    return '#%02x%02x%02x' % RGB

#copied from stackoverflow Alok Singhal
#stackoverflow.com/questions/2272149/round-to-5-or-other-number-in-python
def myround(x, base=5):
    return int(base * round(float(x)/base))

Window = Tk()
Window.title('Canvas')
Canvas = Canvas(Window, width = 1000, height = 1000)
Canvas.pack()

def clear(event='<space>'):
    Canvas.delete('all')
    global i
    i = 0
    global j
    j = 0
Window.bind('<space>', clear)

def run(event='<Key>'):
    #PSize = myround(int(float(input())))
    PSize = int(float(PSizeInput.get()))
    if PSize == 0:
        PSize = 5
    Tolerance = int(TolInput.get())
    clear()
    RGBs = []
    Hexes = []
    RGB = (randint(0, 255), randint(0, 255), randint(0, 255))
    for i in range(int(1000 / PSize)):
        for j in range(int(1000 / PSize)):
            if randint(0, Tolerance) == 0:
                RGB = (randint(0, 255), randint(0, 255), randint(0, 255))
            else:
                if len(RGBs) > (1000 / PSize):
                    if randint(0, 1) == 0:
                        RGB = RGBs[len(RGBs) - int(1000 / PSize)]
                RGB = list(RGB)
                for k in range(2):
                    RGB[k] += randint(-10, 10)
                    if RGB[k] < 0:
                        RGB[k] = 0
                    elif RGB[k] > 255:
                        RGB[k] = 255
                RGB = tuple(RGB)
            RGBs.append(RGB)
            Hex = hex(RGB)
            Hexes.append(Hex)
            IX = j * PSize
            IY = i * PSize
            IIX = (j + 1) * PSize
            IIY = (i + 1) * PSize
            try:
                Pixel = Canvas.create_rectangle(IX, IY, IIX, IIY, fill = Hex,
                                                outline = Hex)
            except:
                Skip = 1
    Window.update()

Controls = Tk()
Controls.geometry('{}x{}'.format(215, 120))
Controls.title('Controls')
Label1 = Text(Controls, height=1, width=10)
Label1.pack()
Label1.insert(END, 'Pixel Size')
PSizeInput = Entry(Controls)
PSizeInput.pack()
Label2 = Text(Controls, height=1, width=10)
Label2.pack()
Label2.insert(END, 'Tolerance')
TolInput = Entry(Controls)
TolInput.pack()
RunButton = Button(Controls, text='Run', command=run).pack()
Controls.bind('<Return>', run)
Controls.bind('<space>', clear)
Window.bind('<Return>', run)
