sum_mans = int(input())
d = {}

for surname in range(sum_mans):
    surnames = input()
    if surnames in d.keys():
        d[surnames] += 1
    else:
        d[surnames] = 1
same_names = []
for num in d.keys():
    if d[num] > 1:
        same_names.append(num)
same_names.sort()
if same_names:
    for num in same_names:
        print(f"{num} - {d[num]}")
else:
    print("Однофамильцев нет")
