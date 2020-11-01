import pdb

class Input:
    def __init__(self, name, value=0):
        self.name = name
        self.value = value

def conv(decimal, base=2, length=8):
    if decimal > 2 ** length:
        raise ValueError('too long for word length (defualt 8)')
    new = ''
    while decimal != 0:
        new = str(decimal % base) + new
        decimal = decimal // base
    new = ('0' * (length - len(new))) + new
    return new

inputs = []
while True:
    new_input = input('New input: ')
    if new_input.upper() == 'NO':
        break
    inputs.append(Input(new_input))
print('')
    

gate = input('Logic statement: \n')
print('')

header = ''
for i in range(len(inputs)):
    header += inputs[i].name + '  '
print(header + 'X')
print('─' * ((len(inputs) * 3) + 1))

for i in range(2 ** len(inputs)):
    val_gate = gate
    i_bin = conv(i, length=len(inputs))
    
    for j in range(len(i_bin)):
        inputs[j].value = i_bin[j]
        print(i_bin[j], end='  ')
        
    for j in range(len(inputs)):
        val_gate = val_gate.replace(inputs[j].name, inputs[j].value)

    try:
        print(int(eval(val_gate)))
    except:
        print('ErrorError: you have a big oof')
    

        
