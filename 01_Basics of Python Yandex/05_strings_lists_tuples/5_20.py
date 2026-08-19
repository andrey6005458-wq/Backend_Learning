def factorial(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


data = list(input().split())
result = [int(data[0])]

for i in data[1:]:
    if i.lstrip("-").isdigit():
        result.append(int(i))
    else:
        if i == "+":
            a = result.pop()
            result[-1] += a
        elif i == "-":
            a = result.pop()
            result[-1] -= a
        elif i == "*":
            a = result.pop()
            result[-1] *= a
        elif i == "/":
            a = result.pop()
            result[-1] //= a
        elif i == "~":
            result[-1] = -result[-1]
        elif i == "#":
            result.append(result[-1])
        elif i == "!":
            result[-1] = factorial(result[-1])
        elif i == "@":
            if len(result) >= 3:
                result.append(result.pop(-3))
            else:
                break

print(result[0])
