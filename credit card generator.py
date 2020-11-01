import random
n = 16

while True:
    print(''.join(["{}".format(random.randint(0, 9)) for num in range(0, n)]))
    input()
