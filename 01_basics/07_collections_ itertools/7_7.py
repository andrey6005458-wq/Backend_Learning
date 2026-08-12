from itertools import combinations

n = int(input())
kids = [input().strip() for _ in range(n)]

for player_1, player_2 in combinations(kids, 2):
    print(f"{player_1} - {player_2}")
