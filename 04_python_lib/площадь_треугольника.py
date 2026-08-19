a, b, c = map(float, input().split())
p = (a + b + c) / 2
s1 = p * (p - a) * (p - b) * (p - c)
s2 = (s1 ** 0.5)
print(s2)