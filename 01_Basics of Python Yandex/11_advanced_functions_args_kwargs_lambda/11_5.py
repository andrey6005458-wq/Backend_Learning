def to_string(*args, **kwargs):
    return kwargs.get("sep", " ").join([str(i) for i in args]) + kwargs.get("end", "\n")


data = [7, 3, 1, "hello", (1, 2, 3)]
result = to_string(*data, sep=", ", end="!")
print(result)
