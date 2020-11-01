with open('words.txt', 'r') as file:
    words = file.read()
    words = eval(words)
    print('Ready')

def check_word(source, word):
    source = source.lower()
    word = word.lower()
    for i in range(len(word)):
        if word[i] in source:
            source = source[:source.index(word[i])] + source[source.index(word[i])+1:]
        else:
            return 0
    return 1

while True:
    pos_words = 0
    source = input('Source? \n')
    for word in words:
        if check_word(source, word):
            print(word)
            pos_words += 1
    print(str(pos_words) + ' words found, ' + str(len(words)) + ' words searched. \n')
