def add(*args):
    x = 0
    for n in args:
        x += n
    return x


#print(add(6, 8, 10, 354, 34, 2))

def calculate(n, **kwargs):
    #print(type(kwargs))
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add = 3, multiply = 5)