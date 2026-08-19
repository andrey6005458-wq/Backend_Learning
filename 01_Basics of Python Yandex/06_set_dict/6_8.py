sum_kids = int(input())
food = {}

for i in range(sum_kids):
    x = input().split()
    for kashas in x[1:]:
        if kashas in food.keys():
            food[kashas].append(x[0])
        else:
            food[kashas] = [x[0]]
kasha = input()
if kasha not in food.keys():
    print("Таких нет")
else:
    print(*sorted(food[kasha]), sep="\n")
