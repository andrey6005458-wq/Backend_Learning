from itertools import permutations

n = int(input())
sportsmens = [input().strip() for _ in range(n)]
for guys in sorted(permutations(sportsmens)):
    print(*guys, sep=", ")
