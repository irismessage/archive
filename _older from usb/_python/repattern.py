from tkinter import *

while True:
    Pass = False
    while not Pass:
        try:
            with open(input('\n Pattern filepath. \n'), 'r') as File:
                Desc = eval(File.read())
                PSize = Desc[0]
                Hexes = Desc[1]
                Pass = True
        except:
            print('Error.')

    Window = Tk()
    Window.title('Canvas')
    Canvas = Canvas(Window, width = 1000, height = 1000)
    Canvas.pack()

    HexNum = 0
    Progress = 0
    print('         ˅')
    for i in range(int(1000 / PSize)):
        for j in range(int(1000 / PSize)):
            Hex = Hexes[HexNum]
            HexNum += 1
            IX = j * PSize
            IY = i * PSize
            IIX = (j + 1) * PSize
            IIY = (i + 1) * PSize
            try:
                Pixel = Canvas.create_rectangle(IX, IY, IIX, IIY, fill = Hex,
                                                outline = Hex)
            except:
                Skip = 1

        NewProgress = int (HexNum / len(Hexes) * 10)
        if NewProgress > Progress:
            Progress = NewProgress
            print('█', end='')

    Window.update()
