from string import ascii_lowercase as alphabet
from random import shuffle

Alphabet = list(alphabet)
Letters = list(alphabet)
shuffle(Letters)

def substitute(String):
    String = str(String).lower()
    NewString = ''
    for i in range(len(String)):
        try:
            NewString += Letters[Alphabet.index(String[i])]
        except:
            if String[i] == ' ':
                NewString += ' '
            else:
                NewString += '?'
    return NewString

while True:
    print(substitute(input()))
        
