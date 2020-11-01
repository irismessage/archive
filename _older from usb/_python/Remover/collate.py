from string import ascii_lowercase as alphabet

letters = list(alphabet)
total = open('dict.txt', 'a')
for letter in letters:
    with open('dict_' + letter + '.txt', 'r') as file:
        total.write('\n'  + str(file.read()))
total.close()
