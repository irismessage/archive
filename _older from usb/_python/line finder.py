import urllib.request

print('© Joel McBride 2017 \n')
print('Instructions: \n' \
      'Input act, scene and line \n' \
      'Press enter to continue from selected point \n' \
      'Press space and then enter to find a new line. \n')

url = 'http://www.folgerdigitaltexts.org/html/Mac.html'

print('Connecting...')
try:
    with urllib.request.urlopen(url) as response:
        script = response.read().decode('utf-8')
        print('Manuscript downloaded')
        print('')
except urllib.error.URLError as err:
    print('No connection.')

def find_line(act, scene, line):
    location = 'title="' + str(act) + '.' + str(scene) + '.' + str(line) + '">'
    new_script = script[script.index(location)+len(location):]
    line_str = new_script[:new_script.index('</span>')]
    line = int(line)
    line -= 1
    if line < 1:
        location = 'name="line-' + str(act) + '.' + str(scene) + '.' + str(line) + '">'
    else:
        location = 'title="' + str(act) + '.' + str(scene) + '.' + str(line) + '">'
    new_script = script[script.index(location)+len(location):]
    idi = 'class="speaker">'
    new_script = new_script[new_script.index(idi)+len(idi):]
    speaker = new_script[:new_script.index('</span>')]
    return speaker + ':    ' + line_str
    
while True:
    act = input('Act: ')
    scene = input('Scene: ')
    line = input('Line: ')
    print('')
##    try:
    print(find_line(act, scene, line), end='')
    while True:
        if input() == ' ':
            break
        else:
            line = int(line)
            line += 1
            try:
                print(find_line(act, scene, line), end='')
            except ValueError:
                print('End of scene.')
                break
##    except ValueError:
##        print('Line not found.')
    print('')
