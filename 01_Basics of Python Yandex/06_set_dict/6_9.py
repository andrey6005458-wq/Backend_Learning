objects = {}
while x := input().split():
    for something in x:
        if something not in objects:
            objects[something] = 1
        else:
            objects[something] += 1
for j in objects:
    print(j, objects[j])
