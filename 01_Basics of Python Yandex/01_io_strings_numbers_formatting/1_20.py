N = int(input())
M = int(input())
K1 = int(input())
K2 = int(input())

вес_первого = N * (M - K2) / (K1 - K2)
вес_второго = N - вес_первого

print(int(вес_первого), int(вес_второго))
