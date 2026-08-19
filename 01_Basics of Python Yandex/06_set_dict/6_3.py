n = int(input())
s = set()
for i in range(n):
    for x in input().split():
        s.add(x)
print(*s, sep="\n")
