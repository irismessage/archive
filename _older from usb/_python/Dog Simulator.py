from random import randint
from time import sleep
Hunger = 0
Happiness = 0
Cleanliness = 0
print("Welcome to Dog Simulator 2015! (Beta 5.0)")
print( )
print('You are going to to adopt a dog. Do you want a male dog or a female dog?')
Gender = input()
if Gender == 'male' or Gender == 'female':
    ValidResponse = True
else:
    ValidResponse = False
while ValidResponse == False:
    print('That is not a valid response. Please try again.')
    Gender = input()
    if Gender == 'male' or Gender == 'female':
        ValidResponse = True
if Gender == 'male':
    HimOrHer = 'him'
else:
    HimOrHer = 'her'
print("You are going to buy a", Gender, 'dog. Now please pick a breed.')
Breed = input()
print('You adopt a',Gender, Breed, '.')
print('What are you going to call it?')
Name = input()
print('You call your', Breed, Name, '.')
sleep(2)
NumberOfBones = 0
print( )

print(Name, 'wants bones. How many are you going to give', HimOrHer, '?')
NumberOfBones = int(NumberOfBones) + int(input())
if (int(NumberOfBones) < 2):
    NotEnoughBones = True
else:
    NotEnoughBones = False
while NotEnoughBones:
    if int(NumberOfBones) == 0:
        print(Name, 'has no bones. Please give', HimOrHer, 'some bones!')
        print('How many are you going to give', HimOrHer, '?')
        NumberOfBones = int(NumberOfBones) + int(input())
    if int(NumberOfBones) == 1:
        print(Name, 'only has one bone. Please give', HimOrHer, 'more bones!')
        print('How many are you going to give', HimOrHer, '?')
        NumberOfBones =int(NumberOfBones) + int(input())
    if (int(NumberOfBones) < 2):
        NotEnoughBones = True
    else:
        NotEnoughBones = False 
print(Name, 'now has', NumberOfBones, 'bones.')
BonesEaten = randint(2, int(NumberOfBones))
if int(BonesEaten) > 100:
    BonesEaten = randint(2, 50)
NumberOfBones = int(NumberOfBones) - int(BonesEaten)
print(Name, 'ate', BonesEaten, 'bones and saved', NumberOfBones, 'for later.')
print('+', BonesEaten, 'Hunger.')
Hunger = int(Hunger) + int(BonesEaten) 
sleep(randint(1, 2))
print( )

print(Name, 'wants to go for a walk.')
print('Where are you going to take him?')
print('The park, the city or the countryside?')
Destination = input()
if Destination == 'the park' or Destination == 'park' or Destination == 'the city' or Destination == 'city' or Destination == 'the countryside' or Destination == 'countryside' or Destination == 'the country' or Destination == 'country':
    ValidResponse = True
else:
    ValidResponse = False
while ValidResponse == False:
    print('That is not a valid response. Please try again.')
    Destination = input()
    if Destination ==  Destination == 'the park' or Destination == 'park' or Destination == 'the city' or Destination == 'city' or Destination == 'the countryside' or Destination == 'countryside' or Destination == 'the country' or Destination == 'country':
        ValidResponse = True
if Destination == 'the park' or Destination == 'park':
    Chance = randint(1, 3)
    if Chance == 1:
        print('You play fetch with', Name, '!')
        print('+ 10 Happiness')
        Happiness = int(Happiness) + 10 
    if Chance == 2:
        print(Name, 'chases a rabbit!')
        print('+ 10 Happiness.')
        Happiness = int(Happiness) + 10 
    if Chance == 3:
        print(Name, 'is scared by a huge Alsatian.')
        print('- 10 Happiness.')
        Happiness = int(Happiness) - 10
elif Destination == 'the city' or Destination == 'city':
    Chance = randint(1, 3)
    if Chance == 1:
        print(Name, 'wees on a lamp post...')
        print('+ 5 Happiness.')
        Happiness = int(Happiness) + 5
    if Chance == 2:
        print('You buy', Name, 'a new toy!')
        print('+ 10 Happiness.')
        Happiness = int(Happiness) + 10
    if Chance == 3:
        print(Name, 'is unhappy about all the loud noise.')
        print('- 5 Happiness.')
        Happiness = int(Happiness) - 5
elif Destination == 'the countryside' or Destination == 'countryside' or Destination == 'the country' or Destination == 'country':
    Chance = randint(1, 3)
    if Chance == 1:
        print(Name, 'has fun running through the fields!')
        print('+ 10 Happiness.')
        Happiness = int(Happiness) + 10
    if Chance == 2:
        print(Name, 'paddles in a stream!')
        print('+ 5 Happiness.')
        Happiness = int(Happiness) + 5
    if Chance == 3:
        print(Name, 'chases some sheep and a farmer shouts at', HimOrHer, '.')
        print('- 5 Happiness.')
        Happiness = int(Happiness) - 5
print('You and', Name, 'return home.')
print('+ 25 Happiness.')
Happiness = int(Happiness) + 25
sleep(randint(1, 2))
print( )

print(Name, 'is dirty! Do you give him a bath?')
GiveBath = input()
if GiveBath == 'yes' or GiveBath == 'no':
    ValidResponse = True
else:
    ValidResponse = False
while ValidResponse == False:
    print('That is not a valid response. Please try again.')
    GiveBath = input()
    if GiveBath == 'yes' or GiveBath == 'no':
        ValidResponse = True
if GiveBath == 'yes':
    print('You try to give', Name, 'a bath...')
    Chance = randint(1, 3)
    if Chance == 1:
        print(Name, 'gets in the bath and is clean.')
        print('+ 10 Cleanliness.')
        Cleanliness = int(Cleanliness) + 10 
    if Chance == 2:
        print(Name, 'has a bath and splashes water on you!')
        print('+ 5 Cleanliness.')
        Cleanliness = int(Cleanliness) + 5
        print('+ 5 Happiness.')
        Happiness = int(Happiness) + 5
    if Chance == 3:
        print(Name, 'does not want a bath and runs away.')
        print('- 20 Cleanliness.')
        Cleanliness = int(Cleanliness) - 20
    if Chance == 1 or 2:
        print(Name, 'is now much cleaner!')
        print('+ 25 Cleanliness.')
        Cleanliness = int(Cleanliness) + 25
else:
    print(Name, 'continues to gather dirt.')
    print('- 20 Cleanliness.')
    Cleanliness = int(Cleanliness) - 20
sleep(randint(1, 2))
print( )


while True:
    print('Hunger:', Hunger)
    print('Happiness:', Happiness)
    print('Cleanliness:', Cleanliness)
    print('To feed', Name, 'press f.')
    print('To take', Name, 'for a walk, press w.')
    print('To give', Name, 'a bath, press b.')
    Option = input()
    if Option == 'f' or Option == 'F' or Option == 'w' or Option == 'W' or Option == 'b'or Option == 'B':
        ValidResponse = True
    else:
        ValidResponse = False
    while ValidResponse == False:
        print('That is not a valid response. Please try again.')
        Option = input()
        if Option == 'f' or Option == 'F' or Option == 'w' or Option == 'W' or Option == 'b'or Option == 'B':
            ValidResponse = True

    if Option == 'f' or Option == 'F':
        print(Name, 'wants bones. How many are you going to give', HimOrHer, '?')
        NumberOfBones = int(NumberOfBones) + int(input())
        if (int(NumberOfBones) < 2):
            NotEnoughBones = True
        else:
            NotEnoughBones = False
        while NotEnoughBones:
            if int(NumberOfBones) == 0:
                print(Name, 'has no bones. Please give', HimOrHer, 'some bones!')
                print('How many are you going to give', HimOrHer, '?')
                NumberOfBones = int(NumberOfBones) + int(input())
            if int(NumberOfBones) == 1:
                print(Name, 'only has one bone. Please give', HimOrHer, 'more bones!')
                print('How many are you going to give', HimOrHer, '?')
                NumberOfBones =int(NumberOfBones) + int(input())
            if (int(NumberOfBones) < 2):
                NotEnoughBones = True
            else:
                NotEnoughBones = False 
        print(Name, 'now has', NumberOfBones, 'bones.')
        BonesEaten = randint(2, int(NumberOfBones))
        if int(BonesEaten) > 100:
            BonesEaten = randint(2, 50)
        NumberOfBones = int(NumberOfBones) - int(BonesEaten)
        print(Name, 'ate', BonesEaten, 'bones and saved', NumberOfBones, 'for later.')
        print('+', BonesEaten, 'Hunger.')
        Hunger = int(Hunger) + int(BonesEaten) 
        sleep(randint(1, 2))
        print( )

    elif Option == 'w' or Option == 'W':
        print(Name, 'wants to go for a walk.')
        print('Where are you going to take him?')
        print('The park, the city or the countryside?')
        Destination = input()
        if Destination == 'the park' or Destination == 'park' or Destination == 'the city' or Destination == 'city' or Destination == 'the countryside' or Destination == 'countryside' or Destination == 'the country' or Destination == 'country':
            ValidResponse = True
        else:
            ValidResponse = False
        while ValidResponse == False:
            print('That is not a valid response. Please try again.')
            Destination = input()
            if Destination == 'the park' or Destination == 'park' or Destination == 'the city' or Destination == 'city' or Destination == 'the countryside' or Destination == 'countryside' or Destination == 'the country' or Destination == 'country':
                ValidResponse = True
        if Destination == 'the park' or Destination == 'park':
            Chance = randint(1, 3)
            if Chance == 1:
                print('You play fetch with', Name, '!')
                print('+ 10 Happiness')
                Happiness = int(Happiness) + 10 
            if Chance == 2:
                print(Name, 'chases a rabbit!')
                print('+ 10 Happiness.')
                Happiness = int(Happiness) + 10 
            if Chance == 3:
                print(Name, 'is scared by a huge Alsatian.')
                print('- 10 Happiness.')
                Happiness = int(Happiness) - 10 
        elif Destination == 'the city' or Destination == 'city':
            Chance = randint(1, 3)
            if Chance == 1:
                print(Name, 'wees on a lamp post...')
                print('+ 5 Happiness.')
                Happiness = int(Happiness) + 5
            if Chance == 2:
                print('You buy', Name, 'a new toy!')
                print('+ 10 Happiness.')
                Happiness = int(Happiness) + 10
            if Chance == 3:
                print(Name, 'is unhappy about all the loud noise.')
                print('- 5 Happiness.')
                Happiness = int(Happiness) - 5
        elif Destination == 'the countryside' or Destination == 'countryside' or Destination == 'the country' or Destination == 'country':
            Chance = randint(1, 3)
            if Chance == 1:
                print(Name, 'has fun running through the fields!')
                print('+ 10 Happiness.')
                Happiness = int(Happiness) + 10
            if Chance == 2:
                print(Name, 'paddles in a stream!')
                print('+ 5 Happiness.')
                Happiness = int(Happiness) + 5
            if Chance == 3:
                print(Name, 'chases some sheep and a farmer shouts at', HimOrHer, '.')
                print('- 5 Happiness.')
                Happiness = int(Happiness) - 5
        print('You and', Name, 'return home.')
        print('+ 25 Happiness.')
        Happiness = int(Happiness) + 25
        sleep(randint(1, 2))
        print( )

    elif Option == 'b' or Option == 'B':
        print(Name, 'is dirty! Do you give him a bath?')
        GiveBath = input()
        if GiveBath == 'yes' or GiveBath == 'no':
            ValidResponse = True
        else:
            ValidResponse = False
        while ValidResponse == False:
            print('That is not a valid response. Please try again.')
            GiveBath = input()
            if GiveBath == 'yes' or GiveBath == 'no':
                ValidResponse = True
        if GiveBath == 'yes':
            print('You try to give', Name, 'a bath...')
            Chance = randint(1, 3)
            if Chance == 1:
                print(Name, 'gets in the bath and is clean.')
                print('+ 10 Cleanliness.')
                Cleanliness = int(Cleanliness) + 10 
            if Chance == 2:
                print(Name, 'has a bath and splashes water on you!')
                print('+ 5 Cleanliness.')
                Cleanliness = int(Cleanliness) + 5
                print('+ 5 Happiness.')
                Happiness = int(Happiness) + 5
            if Chance == 3:
                print(Name, 'does not want a bath and runs away.')
                print('- 20 Cleanliness.')
                Cleanliness = int(Cleanliness) - 20
            if Chance == 1 or 2:
                print(Name, 'is now much cleaner!')
                print('+ 25 Cleanliness.')
                Cleanliness = int(Cleanliness) + 25
        else:
            print(Name, 'continues to gather dirt.')
            print('- 20 Cleanliness.')
            Cleanliness = int(Cleanliness) - 20
        sleep(randint(1, 2))
        print( )
    Hunger = int(Hunger) - randint(1, 10)
    Happiness = int(Happiness) - randint(1, 10)
    Cleanliness = int(Cleanliness) - randint(1, 10)
    
        











                               
    


    
    


 
