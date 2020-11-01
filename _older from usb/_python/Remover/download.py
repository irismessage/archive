import urllib.request
from string import ascii_lowercase as alphabet

letters = list(alphabet)
temp = 'http://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_'
for letter in letters:
    response = urllib.request.urlopen(temp + letter + '.html')
    with open('dict_' + letter + '.txt', 'w+') as file:
        file.write(str(response.read()))
