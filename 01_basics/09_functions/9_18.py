def merge(tuple1, tuple2):
    i = 0
    j = 0
    result = []

    while i < len(tuple1) and j < len(tuple2):
        if tuple1[i] < tuple2[j]:
            result.append(tuple1[i])
            i += 1
        else:
            tuple2[j] < tuple1[i]
            result.append(tuple2[j])
            j += 1

    while i < len(tuple1):
        result.append(tuple1[i])
        i += 1

    while j < len(tuple2):
        result.append(tuple2[j])
        j += 1

    return tuple(result)


result = merge((7, 12), (1, 9, 50))
print(result)
