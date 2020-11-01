filepath = 'directory.txt'

with open(filepath, 'r') as file:
    directory = file.read()
    directory = eval(directory)

def update_directory():
    with open(filepath, 'w') as file:
    file.write(str(directory))

def find_entry():
    while True:
        search_name = input('Name: ')
        for entry in directory:
            if entry['Name'] == search_name:
                return entry

def add():
    while True:
        if input() == 'quit':
            break
        
        new_place = {}
        new_place['Name'] = input('Place Name: ')
        new_place['Type'] = input('Type of Place: ')
        new_place['Owner'] = input('Owner: ')
        new_place['Area'] = input('Area: ')
        new_place['Coords'] = (input('X: '), input('Y: '), input('Z: '))
        directory.append(new_place)

        update_directory()

def edit():
    while True:
        entry = find_entry()
        attribute = input('Attrbiute to edit: ')
        entry[attribute] = input('New value: ')
            
def read():
    entry = find_entry()
    print('Name: ' + entry['Name'])
    print('Type: ' + entry['Type'])
    print('Owner: ' + entry['Owner'])
    print('Area: ' + entry['Area'])
    print('Coords: ' + entry['Cords'])

while True:
    choice = input('What do you want to do?')

    if choice = 'quit':
        break
    elif choice = 'add':
        new()
    elif choice = 'edit':
        edit()
    elif choice = 'read':
        read()
    else:
        print('Invalid input.')





