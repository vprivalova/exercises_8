line = list(input())
i = int(input())
j = int(input())


def filter_is_upper(letter):
    if letter.isupper() is True:
        return True
    else:
        return False


only_uppers = filter(filter_is_upper, line[i-1:j])
print(len(list(only_uppers)))
