from random import randint
print('Welcome to enCode!(Encrypter)')
print('Please select a encryption code, or press R for a random code.')
PIN = input()
if PIN == 'r' or PIN == 'R':
    PIN = randint(1000, 9999)
    print('Your randomised code is', PIN)
print('Now, please indavidually type each letter you want encrypted.')
print('Please use all caps and no punctuation.')
print('After each letter, press enter.')
print('When you are done, type END, then press enter.')

Num = 0
TempC = 0
Stop = False
Letters = [0]
CDLetters = [0]
while Stop == False:
    Letters.insert(Num, input())
    if Letters[Num] == 'A':
        TempRec = 1
    elif Letters[Num] == 'B':
        TempRec = 2
    elif Letters[Num] == 'C':
        TempRec = 3
    elif Letters[Num] == 'D':
        TempRec = 4
    elif Letters[Num] == 'E':
        TempRec = 5
    elif Letters[Num] == 'F':
        TempRec = 6
    elif Letters[Num] == 'G':
        TempRec = 7
    elif Letters[Num] == 'H':
        TempRec = 8
    elif Letters[Num] == 'I':
        TempRec = 9
    elif Letters[Num] == 'J':
        TempRec = 10
    elif Letters[Num] == 'K':
        TempRec = 11
    elif Letters[Num] == 'L':
        TempRec = 12
    elif Letters[Num] == 'M':
        TempRec = 13
    elif Letters[Num] == 'N':
        TempRec = 14
    elif Letters[Num] == 'O':
        TempRec = 15
    elif Letters[Num] == 'P':
        TempRec = 16
    elif Letters[Num] == 'Q':
        TempRec = 17
    elif Letters[Num] == 'R':
        TempRec = 18
    elif Letters[Num] == 'S':
        TempRec = 19
    elif Letters[Num] == 'T':
        TempRec = 20
    elif Letters[Num] == 'U':
        TempRec = 21
    elif Letters[Num] == 'V':
        TempRec = 22
    elif Letters[Num] == 'W':
        TempRec = 23
    elif Letters[Num] == 'X':
        TempRec = 24
    elif Letters[Num] == 'Y':
        TempRec = 25
    elif Letters[Num] == 'Z':
        TempRec = 26
    else:
        TempC = Letters[Num]

    TempRec = int(TempRec) + int(PIN)

    while int(TempRec) > 26:
        TempRec = int(TempRec) - 26

    if TempRec == 1:
        CDLetters.insert(Num, 'A')
    elif TempRec == 2:
        CDLetters.insert(Num, 'B')
    elif TempRec == 3:
        CDLetters.insert(Num, 'C')
    elif TempRec == 4:
        CDLetters.insert(Num, 'D')
    elif TempRec == 5:
        CDLetters.insert(Num, 'E')
    elif TempRec == 6:
        CDLetters.insert(Num, 'F')
    elif TempRec == 7:
        CDLetters.insert(Num, 'G')
    elif TempRec == 8:
        CDLetters.insert(Num, 'H')
    elif TempRec == 9:
        CDLetters.insert(Num, 'I')
    elif TempRec == 10:
        CDLetters.insert(Num, 'J')
    elif TempRec == 11:
        CDLetters.insert(Num, 'K')
    elif TempRec == 12:
        CDLetters.insert(Num, 'L')
    elif TempRec == 13:
        CDLetters.insert(Num, 'M')
    elif TempRec == 14:
        CDLetters.insert(Num, 'N')
    elif TempRec == 15:
        CDLetters.insert(Num, 'O')
    elif TempRec == 16:
        CDLetters.insert(Num, 'P')
    elif TempRec == 17:
        CDLetters.insert(Num, 'Q')
    elif TempRec == 18:
        CDLetters.insert(Num, 'R')
    elif TempRec == 19:
        CDLetters.insert(Num, 'S')
    elif TempRec == 20:
        CDLetters.insert(Num, 'T')
    elif TempRec == 21:
        CDLetters.insert(Num, 'U')
    elif TempRec == 22:
        CDLetters.insert(Num, 'V')
    elif TempRec == 23:
        CDLetters.insert(Num, 'W')
    elif TempRec == 24:
        CDLetters.insert(Num, 'X')
    elif TempRec == 25:
        CDLetters.insert(Num, 'Y')
    elif TempRec == 26:
        CDLetters.insert(Num, 'Z')
    else:
        CDLetters.insert(Num, TempC)

    if Letters[Num] == 'END':
        Stop = True

    Num = int(Num) + 1

print('Your encrypted message is:', CDLetters, end = '.')
print('Just give this along with your decryption code to whoever you want to decode it.')
print('They can use the decrypter to decrypt it.')
        

    
    
        
    
    
    
