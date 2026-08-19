n = int(input())
print("А Б В")

for a in range(1, n):
    for b in range(1, n):
        for c in range(1, n):
            sum = a + b + c
            if sum == n:
                print(a, b, c)
