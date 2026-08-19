data = {"a": [1, 2, 3], "b": [5, 2, 5], "c": [7, 15, 3]}
answer = {key for key, values in data.items() if len(values) != len(set(values))}
print(answer)
