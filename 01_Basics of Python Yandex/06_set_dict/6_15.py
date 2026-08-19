numbers = list(map(int, input().split()))
result = []

for num in numbers:
    s = bin(num)[2:]  # двоичное представление без '0b'
    digits = len(s)
    units = s.count("1")
    zeros = s.count("0")

    result.append({"digits": digits, "units": units, "zeros": zeros})

print(result)
