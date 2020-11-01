from urllib import request

URL = input('Enter URL \n')
while True:
    response = request.urlopen(URL)
    html = str(response.read())
##    startpoint = html.index('<div id="Bz9XYicV0OVRJxZOYMwj98WHpnzgJ4x8" style="width:400px;font-size:40px;margin:auto;padding:18px;background-color:#333;color:#fff;-webkit-border-radius:4px;-moz-border-radius:4px;border-radius:4px;margin-bottom:10px;">')
##    print(html[startpoint:startpoint + 10])
    print(html)
