text = list(input().split())
result = [int(text[0])]
for i in text[1:]:
    if i.isdigit():
        result.append(int(i))
    else:
        a = result.pop()
        if i == "+":
            result[-1] += a
        elif i == "-":
            result[-1] -= a
        elif i == "*":
            result[-1] *= a
        else:
            result[-1] /= a
print(result[0])
