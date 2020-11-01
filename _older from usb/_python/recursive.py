def add_one(num):
    num = add_two(num)
    num -= 1
    return num

def add_two(num):
    for i in range(2):
        num = add_one(num)
    return num

add_one(1)

##try:
##    add_one(input())
##except:
##    from sys import exc_info
##    print(exc_info())
    
