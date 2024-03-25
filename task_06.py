def decorator(func):
    def wrapped(arg):
        print(func(arg))
    return wrapped


@decorator
def square_root(num):
    root = round(num**0.5, 2)
    return root


@decorator
def reversing(line):
    result = line[::-1]
    return result


square_root(906)
reversing('apple')
