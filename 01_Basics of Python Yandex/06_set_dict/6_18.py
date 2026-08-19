n = int(input())
d = {}
for i in range(n):
    x, y = map(int, input().split())
    x //= 10
    y //= 10
    if (x, y) in d.keys():
        d[(x, y)] += 1
    else:
        d[(x, y)] = 1

print(max(d.values()))
print(d)
