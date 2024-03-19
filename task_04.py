import functools

a, b, c = map(int, input().split())

only_suitable = filter(lambda x: (x % c == 0 and (x**0.5).is_integer() is True), list(range(a, b + 1)))

result = functools.reduce(lambda x, y: x*y, list(only_suitable))
print(result)
