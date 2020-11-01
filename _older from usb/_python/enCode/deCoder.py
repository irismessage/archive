from random import randint
print('Welcome to enCode (Decrypter)')
print('Please enter your decryption PIN.')
PIN = input()
print('Now, please indavidually type each letter you want decrypted.')
print('Please use all caps and no punctuation.')
print('After each letter, press enter.')
print('When you are done, type END, then press enter.')

Num = 0
TempC = 0
Stop = False
Letters = [0]
CDLetters = [0]
while Stop == False:
    CDLetters.insert(Num, input())
    if CDLetters[Num] == 'A':
        TempRec = '1'
    elif CDLetters[Num] == 'B':
        TempRec = '2'
    elif CDLetters[Num] == 'C':
        TempRec = '3'
    elif CDLetters[Num] == 'D':
        TempRec = '4'
    elif CDLetters[Num] == 'E':
        TempRec = '5'
    elif CDLetters[Num] == 'F':
        TempRec = '6'
    elif CDLetters[Num] == 'G':
        TempRec = '7'
    elif CDLetters[Num] == 'H':
        TempRec = '8'
    elif CDLetters[Num] == 'I':
        TempRec = '9'
    elif CDLetters[Num] == 'J':
        TempRec = '10'
    elif CDLetters[Num] == 'K':
        TempRec = '11'
    elif CDLetters[Num] == 'L':
        TempRec = '12'
    elif CDLetters[Num] == 'M':
        TempRec = '13'
    elif CDLetters[Num] == 'N':
        TempRec = '14'
    elif CDLetters[Num] == 'O':
        TempRec = '15'
    elif CDLetters[Num] == 'P':
        TempRec = '16'
    elif CDLetters[Num] == 'Q':
        TempRec = '17'
    elif CDLetters[Num] == 'R':
        TempRec = '18'
    elif CDLetters[Num] == 'S':
        TempRec = '19'
    elif CDLetters[Num] == 'T':
        TempRec = '20'
    elif CDLetters[Num] == 'U':
        TempRec = '21'
    elif CDLetters[Num] == 'V':
        TempRec = '22'
    elif CDLetters[Num] == 'W':
        TempRec = '23'
    elif CDLetters[Num] == 'X':
        TempRec = '24'
    elif CDLetters[Num] == 'Y':
        TempRec = '25'
    elif CDLetters[Num] == 'Z':
        TempRec = '26'
    else:
        TempC = CDLetters[Num]

    TempRec = int(TempRec) - int(PIN)

    while int(TempRec) < 1:
        TempRec = int(TempRec) + 26

    if TempRec == 1:
        Letters.insert(Num, 'A')
    elif TempRec == 2:
        Letters.insert(Num, 'B')
    elif TempRec == 3:
        Letters.insert(Num, 'C')
    elif TempRec == 4:
        Letters.insert(Num, 'D')
    elif TempRec == 5:
        Letters.insert(Num, 'E')
    elif TempRec == 6:
        Letters.insert(Num, 'F')
    elif TempRec == 7:
        Letters.insert(Num, 'G')
    elif TempRec == 8:
        Letters.insert(Num, 'H')
    elif TempRec == 9:
        Letters.insert(Num, 'I')
    elif TempRec == 10:
        Letters.insert(Num, 'J')
    elif TempRec == 11:
        Letters.insert(Num, 'K')
    elif TempRec == 12:
        Letters.insert(Num, 'L')
    elif TempRec == 13:
        Letters.insert(Num, 'M')
    elif TempRec == 14:
        Letters.insert(Num, 'N')
    elif TempRec == 15:
        Letters.insert(Num, 'O')
    elif TempRec == 16:
        Letters.insert(Num, 'P')
    elif TempRec == 17:
        Letters.insert(Num, 'Q')
    elif TempRec == 18:
        Letters.insert(Num, 'R')
    elif TempRec == 19:
        Letters.insert(Num, 'S')
    elif TempRec == 20:
        Letters.insert(Num, 'T')
    elif TempRec == 21:
        Letters.insert(Num, 'U')
    elif TempRec == 22:
        Letters.insert(Num, 'V')
    elif TempRec == 23:
        Letters.insert(Num, 'W')
    elif TempRec == 24:
        Letters.insert(Num, 'X')
    elif TempRec == 25:
        Letters.insert(Num, 'Y')
    elif TempRec == 26:
        Letters.insert(Num, 'Z')
    else:
        Letters.insert(Num, TempC)

    if Letters[Num] == 'END':
        Stop = True

    Num = int(Num) + 1

print('Your decrypted message is', Letters, end = '.')
print('Thank you for using enCode')
