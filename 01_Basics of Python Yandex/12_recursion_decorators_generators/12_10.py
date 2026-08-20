def make_linear(line):
    new_line = []
    for i in line:
        if isinstance(i, list):
            new_line.extend(make_linear(i))
        else:
            new_line.append(i)
    return new_line


result = make_linear([1, 2, [3]])
print(result)
