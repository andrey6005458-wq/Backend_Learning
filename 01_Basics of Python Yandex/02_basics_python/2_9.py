name1 = input()
name2 = input()
name3 = input()

if name1 < name2 and name1 < name3:
    print(name1)
elif name2 < name1 and name2 < name3:
    print(name2)
else:
    print(name3)
