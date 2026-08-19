n = int(input())
pages = []

for i in range(n):
    pages.append(input())
find = input()
for x in pages:
    if find.lower() in x.lower():
        print(x)
