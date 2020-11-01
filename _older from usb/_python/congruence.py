from tkinter import *
import turtle


line1_min = 0
line1_max = 300
line2_min = 0
line2_max = 300
angle_min = 0
angle_max = 360

origin = 250
xorigin = 250
yorigin = 100


window = Tk()
window.title('Canvas')
canvas = Canvas(window, width=500, height=500)
canvas.pack()


controls = Tk()
controls.geometry('{}x{}'.format(215, 200))
controls.title('Controls')

label1 = Text(controls, height=1, width=10)
label1.pack()
label1.insert(END, 'Line 1')
line1_slider = Scale(controls, from_=line1_min, to=line1_max, orient='horizontal')
line1_slider.pack()

label2 = Text(controls, height=1, width=10)
label2.pack()
label2.insert(END, 'Line 2')
line2_slider = Scale(controls, from_=line2_min, to=line2_max, orient='horizontal')
line2_slider.pack()

label3 = Text(controls, height=1, width=10)
label3.pack()
label3.insert(END, 'Angle')
angle_slider = Scale(controls, from_=angle_min, to=angle_max, orient='horizontal')
angle_slider.pack()


def delc(element):
    canvas.delete(element)


turtle.mode('logo')
def get(start_x, start_y, angle, distance):
    turtle.penup()
    turtle.speed(speed=0)
    
    turtle.setpos(start_x, start_y)
    turtle.setheading(-angle)
    turtle.forward(distance)

    return turtle.xcor(), turtle.ycor()


angle = 0
line1_length = 0
line2_length = 0
line1 = canvas.create_line(0, 0, 0, 0)
line2 = canvas.create_line(0, 0, 0, 0)
linex = canvas.create_line(xorigin, yorigin, 250, 500)
def update():
    global angle
    global line1_length
    global line2_length
    global line1
    global line2
    
    if angle != angle_slider.get():
        delc(line1)
        angle = angle_slider.get()
        x, y = get(xorigin, yorigin, angle, line1_length)
        line1 = canvas.create_line(xorigin, yorigin, x, y)

        delc(line2)
        line2_length = line2_slider.get()
        x, y = get(xorigin, yorigin, angle, line1_length)
        x1, y1 = get(x, y, 135, line2_length)
        x2, y2 = get(x, y, -45, line2_length)
        line2 = canvas.create_oval(x1, y1, x2, y2)
        
    if line1_length != line1_slider.get():
        delc(line1)
        line1_length = line1_slider.get()
        x, y = get(xorigin, yorigin, angle, line1_length)
        line1 = canvas.create_line(xorigin, yorigin, x, y)

        delc(line2)
        line2_length = line2_slider.get()
        x, y = get(xorigin, yorigin, angle, line1_length)
        x1, y1 = get(x, y, 135, line2_length)
        x2, y2 = get(x, y, -45, line2_length)
        line2 = canvas.create_oval(x1, y1, x2, y2)
        
    if line2_length != line2_slider.get():
        delc(line2)
        line2_length = line2_slider.get()
        x, y = get(xorigin, yorigin, angle, line1_length)
        x1, y1 = get(x, y, 135, line2_length)
        x2, y2 = get(x, y, -45, line2_length)
        line2 = canvas.create_oval(x1, y1, x2, y2)
    
    canvas.update()


while True:
    update()

