def conv(decimal, base=2, length=8):
    if decimal > 2 ** length:
        raise ValueError('too long for word length (defualt 8)')
    new = ''
    while decimal != 0:
        new = str(decimal % base) + new
        decimal = decimal // base
    new = ('0' * (length - len(new))) + new
    return new

while True:
    print(conv(int(input())))
