with open('listdict.txt', 'r') as file:
    listdict = file.read()
    dictionary = eval(listdict)
print('Ready')

def get_all_defs(word):
    while True:
        print(dictionary[word])
        del dictionary[word]

while True:
##    try:
    get_all_defs(input())
##    except:
##        print('No defs')
##        continue
