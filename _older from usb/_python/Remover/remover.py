with open('listdict.txt', 'r') as file:
    listdict = file.read()
    dictionary = eval(listdict)

while True:
    passage = input()
    passagelist = passage.split()
    for word in passagelist:
        try:
            if 'a.' in dictionary[str.upper(word[0])+str.lower(word[1:])]['type']:
                passagelist.delete(passagelist.index(word))
        except:
            continue
    print(str(passagelist))
