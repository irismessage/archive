code = """
LOLLO OOLOO OLOLL OLOLL OOOLL OLLLO OLLOL OOLOO LOOLL O
OLLL OOLOO OOLOL OLOLL OOOOO OOLLO OLO
OO LOOLO OLLLL OLOLL OOOLL LOOLO OLLLO OLOLO OO
LOO OLOOO OLOOL OLLOO LOOLO OLOL
O OLLLO OOLOO OOLOO LOOLO LOOLO
"""

swaps = {"\n": "",
         "L": "1",
         "O": "0"}
swaps2 = {"\n": "",
         "O": "1",
         "L": "0"}

# I feel like it should be Baudot, but it's not working.
# Maybe the scraps of paper are all upside down?
# Let's try reversing the message.
code = code[::-1]


# Swap out L's and O's for 1's and 0's.
new_code = code
for orig in swaps.keys():
    new_code = new_code.replace(orig, swaps[orig])
    
print("L->1 O->0")
print(new_code)


# Try swapping out the other way round.
new_code2 = code
for orig in swaps2.keys():
    new_code2 = new_code2.replace(orig, swaps2[orig])
    
print("O->1 L->0")
print(new_code2)


# Try padding out to make each 5-bit block a byte.
padding = 3 
padded_new_code = "0"*padding + new_code.replace(" ", " " + "0"*padding)

print("padded")
print(padded_new_code)
# nope.


# Idea: Baudot code?
