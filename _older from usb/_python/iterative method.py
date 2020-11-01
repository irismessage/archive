def iterate(num, func):
    print(num)
    if func(num) == num:
        return num
    else:
        return iterate(func(num), func)

def f(x):
    #example
    return x**2 + x * 3 + 17

print(iterate(int(input()), f))
