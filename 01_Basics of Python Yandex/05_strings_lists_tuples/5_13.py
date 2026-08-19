n = int(input())
digit = []

for i in range(n):
    digit.append(int(input()))
stage = int(input())
for num in digit:
    print(num**stage)
