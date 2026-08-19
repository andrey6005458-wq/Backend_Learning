def split_numbers(text):
    return tuple(map(int, text.split()))


result = split_numbers("1 2 3 4 5")
print(result)
