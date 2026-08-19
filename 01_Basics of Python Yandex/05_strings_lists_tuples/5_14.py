digits = list(map(int, input().split()))
stage = int(input())

for num in digits:
    print(num**stage, end=" ")
