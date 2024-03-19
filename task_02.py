a, b, c, d = map(int, input().split())

only_multiplies = filter(lambda x: (x%c ==0 and x%d ==0), list(range(a, b + 1)))

result = 0

for elem in list(only_multiplies):
    result = result + elem

print(result)
