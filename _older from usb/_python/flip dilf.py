def encode(text):
    new_text = ''
    
    for char in text:
        point = ord(char)
        tniop = str(point)[::-1]
        binary = format(int(tniop), 'b')
        yranib = str(binary)[::-1]
        print(yranib)
        
        new_char = chr(int(format(int(yranib), 'd')))
        new_text += new_char

    return new_text

while True:
    print(encode(input()))
