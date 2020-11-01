from winsound import Beep
import msvcrt

def f(n):
    AFOUR = 440
    return int((2 ** (n / 12)) * AFOUR)

#c4 -9
#d4 -7
#e4 -5
#f4 -4
#g4 -2
#b4 2

mary_little_lamb = [-5, -7, -9, -7, -5, -5, -5,
                    -5, -7, -7, -5, -7, -9]

song = mary_little_lamb
i = 0
while True:
    note = song[i]
    if msvcrt.kbhit():
        Beep(1000, f(note))

    if i == len(song):
        break
    else:
        i += 1
