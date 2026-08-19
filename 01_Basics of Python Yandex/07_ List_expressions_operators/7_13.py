data = {"a": [100], "b": [20, 5], "c": [7, 15, 3]}
answer = min(data, key=lambda k: (sum(data[k]), k))
print(answer)
