from tkinter import *
from random import randint, shuffle
from math import factorial, sqrt
from time import sleep

window = Tk()
canvas = Canvas(window, width=1000, height=1000)
canvas.pack()

lines = []
def add_to_route(a, b, show=True):
    global canvas
    global lines
    global solutions
    global total_distance
    if show:
        lines.append(canvas.create_line(a[0], a[1], b[0], b[1]))
    x_distance = abs(a[0] - b[0])
    y_distance = abs(a[1] - b[1])
    sum_of_squares = x_distance**2 + y_distance**2
    distance = sqrt(sum_of_squares)
    total_distance += distance

while True:
    solutions = {}
    solution_lengths = []
    canvas.delete('all')
        
    num_of_places = randint(4, 6)
    places = []
    for i in range(num_of_places):
        places.append((randint(1, 1000), randint(1, 1000)))

    for place in places:
        drawn_place = canvas.create_rectangle(place[0], place[1],
                                            place[0]+10, place[1]+10,
                                            fill='black', outline='black')
    canvas.update()
    sequences = []
    while len(sequences) < factorial(num_of_places):
        sequence = list(range(num_of_places))
        shuffle(sequence)
        if not sequence in sequences:
            sequences.append(sequence)
    print('Generated all sequences, testing')
    
    for sequence in sequences:
        total_distance = 0
        for i in range(0, num_of_places-1):
            add_to_route(places[sequence[i]], places[sequence[i+1]])
        canvas.update()
##        print(sequence)
##        print(total_distance)
        solutions[str(total_distance)] = sequence
        solution_lengths.append(total_distance)
        canvas.delete('all')
        for place in places:
            drawn_place = canvas.create_rectangle(place[0], place[1],
                                                place[0]+10, place[1]+10,
                                                fill='black', outline='black')
    solution_lengths.sort()
    best_sequence = solutions[str(solution_lengths[0])]
    print('Fastest route is: ' + str(best_sequence))
    for i in range(0, num_of_places-1):
        add_to_route(places[best_sequence[i]], places[best_sequence[i+1]], show=True)
    sleep(0.1)
    canvas.update()
                                  
    input()
