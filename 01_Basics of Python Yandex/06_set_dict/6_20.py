data = sorted(map(int, input().split("; ")))
result = dict.fromkeys(data)
for i in data:
    for j in data:
        a, b = i, j
        while b:
            a, b = b, a % b
        if a == 1:
            if result[i]:
                result[i].add(j)
            else:
                result[i] = {j}
for number in result:
    if result[number]:
        print(f'{number} - {", ".join(map(str, sorted(result[number])))}')
