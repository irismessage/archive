try:
    MaxWordLength = 7
    WordsPerPass = 3

    from random import randint, choice
    from tkinter import *

    DictFile = open('words.txt', 'r')
    DictTxt = DictFile.read()
    Dict = eval(DictTxt)

    def gen():
        Password = ''
        
        for i in range(WordsPerPass):
            while True:
                Word = choice(Dict)
                if len(Word) < MaxWordLength:
                    break
            Word = Word[0].upper() + Word[1:]
            Password += Word
            
        Number = str(randint(0, 99))
        if len(Number) == 1:
            Number = '0' + Number
        Password += Number

        Text.delete(0.0, END)
        Text.insert(END, Password)

    Window = Tk()

    Text = Text(Window, width=23, height=1)
    Button = Button(Window, text='Generate a password', command=gen)

    Text.pack()
    Button.pack()
except:
    from sys import exc_info
    print(exc_info())
    delay = input()
