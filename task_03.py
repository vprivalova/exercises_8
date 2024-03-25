a, b, c, d = map(int, input().split())

data = list(range(a, b + 1))
only_special = map(lambda x: True if (x % c != 0 and str(x)[-1] == str(d)) else False, data)

print(list(only_special).count(True))
