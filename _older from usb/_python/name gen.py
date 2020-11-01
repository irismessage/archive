from random import randint, seed, choice

vowels = 'aeiou'
v = list(vowels)
consonants = 'bcdfghjklmnpqrstvwxyz'
c = list(consonants)

seed(input('Seed? \n'))

def gen_name(pairs):
    name = ''
    for i in range(pairs):
        if randint(0, 1) == 0:
            name += choice(c)
            name += choice(v)
        else:
            name += choice(v)
            name += choice(c)

    name = name[0].upper() + name[1:]
    
    return name

batch = 1
while True:
    delay = input()
    if not delay == '':
        batch = int(delay)
    for i in range(batch):
        print(gen_name(randint(2,4)))
