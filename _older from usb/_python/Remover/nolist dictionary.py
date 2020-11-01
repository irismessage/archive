def get_defs(word):
    with open('dict.txt', 'r') as file:
        textdict = file.read()
        listdefs = []
    while word in textdict:
        textdict = textdict[textdict.index(word):]
        listdefs.append(textdict[:textdict.index('</P>')])
    return listdefs

while True:
    print(get_defs(input()))
