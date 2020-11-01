from tkinter import *

size = 2
width = 255

root = Tk()
canvas = Canvas(root, width=width*size, height=width*size)
canvas.pack()

#0 for red 1 for green 2 for blue
constant = 2
value = 255
for y in range(width):
    for x in range(width):
        array = [x, y]
        array.insert(constant, 0)
        hex = "#{0:02x}{1:02x}{2:02x}".format(array[0], array[1], array[2])
        new_rect = canvas.create_rectangle(x*size, y*size,
                                           (x+1)*size, (y+1)*size,
                                           fill=hex, width=0)

root.mainloop()
