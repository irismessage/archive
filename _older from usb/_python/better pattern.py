from tkinter import *
from time import sleep
from random import randint, choice

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

Hexes = []
PSize = 0
def run(event='<Key>'):
    Props = []
    global PSize
    PSize = int(float(PSizeInput.get()))
    for Direc in list(PropSelect.curselection()):
        if Direc == 3:
            Props.append(int(1000 / PSize) - (int(1000 / PSize) * 2) + 1)
        else:
            Props.append(Direc - 1)
    #PSize = myround(int(float(input())))
    if PSize == 0:
        PSize = 1
    Tolerance = int(TolInput.get())
    clear()
    Window.update()
    RGBs = []
    global Hexes
    Hexes = []
    if BaseInput.get() == '' or BaseInput.get() == 'RANDOM':
        RGB = (randint(0, 255), randint(0, 255), randint(0, 255))
    else:
        RGB = eval(BaseInput.get())
    i = 0
    j = 0
    for i in range(10000):
        if randint(0, Tolerance) == 0:
            i = randint(0, 1000)
            j = randint(0, 1000)
        else:
            i += choice([-1, 1])
            if i < 0:
                i = 0
            elif i > 1000:
                i = 1000
            j += choice([-1, 1])
            if j < 0:
                j = 0
            elif j > 1000:
                j = 1000
        if randint(0, Tolerance) == 0:
            RGB = (randint(0, 255), randint(0, 255), randint(0, 255))
        else:
            if len(RGBs) > (1000 / PSize):
                RGB = RGBs[len(RGBs)-(int(1000 / PSize)+choice(Props))]
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
    Window.update()

def pickbase():
    Chosen = colorchooser.askcolor()
    Chosen = list(Chosen)
    BaseInput.delete(0, END)
    BaseInput.insert(END, str(Chosen[0]))

def save(event='s'):
    i = 1
    while True:
        try:
            TestFile = open('pattern' + str(i) + '.txt', 'r')
            i += 1
        except:
            break
    global PSize
    global Hexes
    Desc = [PSize, Hexes]
    with open('pattern' + str(i) + '.txt', 'w+') as File:
        File.write(str(Desc))

Controls = Tk()
Controls.geometry('{}x{}'.format(215, 250))
Controls.title('Controls')

Label1 = Text(Controls, height=1, width=10)
Label1.pack()
Label1.insert(END, 'Pixel Size')
PSizeInput = Entry(Controls)
PSizeInput.pack()
PSizeInput.insert(END, 10)

Label2 = Text(Controls, height=1, width=10)
Label2.pack()
Label2.insert(END, 'Tolerance')
TolInput = Entry(Controls)
TolInput.pack()
TolInput.insert(END, 100000)

PropSelect = Listbox(Controls, height=4, selectmode=MULTIPLE)
PropSelect.pack()
for Box in ['Diagonal right', 'Down', 'Diagonal left', 'Right']:
    PropSelect.insert(END, Box)
PropSelect.select_set(1, 3)

Label3 = Text(Controls, height=1, width=10)
Label3.pack()
Label3.insert(END, 'Base Hue')
BaseInput = Entry(Controls)
BaseInput.pack()
BaseInput.insert(END, 'RANDOM')

PickButton = Button(Controls, text='Pick Colour', command=pickbase).pack()
RunButton = Button(Controls, text='Run', command=run).pack()
Controls.bind('<Return>', run)
Controls.bind('<space>', clear)
Controls.bind('s', save)
Window.bind('<Return>', run)
