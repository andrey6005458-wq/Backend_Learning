friends = {}
while x := input().split():
    if x[0] not in friends:
        friends[x[0]] = {x[1]}
    else:
        friends[x[0]].add(x[1])
    if x[1] not in friends:
        friends[x[1]] = {x[0]}
    else:
        friends[x[1]].add(x[0])
friends_2 = dict.fromkeys(friends, set())
for friend in friends:
    for n in friends[friend]:
        friends_2[friend] = friends_2[friend].union(friends[n])
    friends_2[friend].discard(friend)
    for z in friends[friend]:
        friends_2[friend].discard(z)
data = []
for friend in friends_2:
    data.append(f'{friend}: {", ".join(sorted(friends_2[friend]))}')
data.sort()
for string in data:
    print(string)
