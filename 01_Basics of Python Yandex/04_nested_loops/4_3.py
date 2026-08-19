n = int(input())

current = 1
row_length = 1

while current <= n:
    for i in range(row_length):
        print(current, end=" ")
        current += 1
        if current > n:
            break
    print()
    row_length += 1
