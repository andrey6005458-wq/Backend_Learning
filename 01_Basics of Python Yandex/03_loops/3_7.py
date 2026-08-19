a = int(input())
b = int(input())

a1 = a
b1 = b

while b:
    a, b = b, a % b

nod = a
nok = (a1 * b1) // nod

print(nok)
