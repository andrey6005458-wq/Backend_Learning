n = int(input())
m = int(input())
dlina = m * n + (n - 1)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j == 1:
            print(f"{i * j:^{m}}", end="")
        else:
            print(f"|{i * j:^{m}}", end="")
    print()
    if i != n:
        print("-" * dlina)
