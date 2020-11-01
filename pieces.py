num = 3
while True:
    divs = 0
    for i in range(1, num):
        if num % i == 0:
            divs += 1
    match = divs / num * 100
    if match == 100:
        print('MATCH: ' + str(num), end='')
    print(str(num) + ': ' + str(match), end='')
    input()

    num += 1
