a, b, c, d = map(int, input().split())

only_special = filter(lambda x: (x % c != 0 and str(x)[-1] == str(d)), list(range(a, b + 1)))

print(len(list(only_special)))
