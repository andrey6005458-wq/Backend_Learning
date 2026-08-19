digits = list(map(int, input().split()))

nod = digits[0]

for num in digits[1:]:
    a = nod
    b = num
    while b:
        a, b = b, a % b
    nod = a

print(nod)
