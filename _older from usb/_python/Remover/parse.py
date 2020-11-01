with open('dict.txt', 'r') as file:
    dicti = file.read()

file = open('listdict.txt', 'a+')
file.write('{')
while '<P>' in dicti:
    wordtype = dicti[dicti.index('<I>')+3:dicti.index('</I>')]
    worddef = dicti[dicti.index('</I>')+5:dicti.index('</P>')]
    formdef = {'type': wordtype, 'definition': worddef}
    file.write("'")
    file.write(dicti[dicti.index('<B>')+3:dicti.index('</B>')])
    file.write("': ")
    file.write(str(formdef))
    file.write(', ')
    dicti = dicti[dicti.index('</P>') + 4:]
file.write('}')
file.close()
