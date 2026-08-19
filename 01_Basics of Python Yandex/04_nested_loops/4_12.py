h = int(input())
m = int(input())
lenght = len(str(h * m))

current = 0

for i in range(h):
    for j in range(m):
        current += 1
        print(f"{current:>{lenght}}", end=" ")
    print()
