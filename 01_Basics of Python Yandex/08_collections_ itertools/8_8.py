from itertools import cycle, islice

n = int(input())
kashas = [input().strip() for _ in range(n)]
days = int(input())
for food in islice(cycle(kashas), days):
    print(food)
