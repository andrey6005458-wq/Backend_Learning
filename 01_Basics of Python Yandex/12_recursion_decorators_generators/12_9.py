def cycle(line):
    while line:
        for i in line:
            yield i


print(*(x for _, x in zip(range(5), cycle([1, 2, 3]))))
