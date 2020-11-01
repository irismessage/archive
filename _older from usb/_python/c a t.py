from urllib import request

response = request.urlopen('http://www.st-pauls.leicester.sch.uk/')
html = response.read()

html.replace('src=" %s "'

with open('C A T', 'w+') as file:
    file.write(html)
