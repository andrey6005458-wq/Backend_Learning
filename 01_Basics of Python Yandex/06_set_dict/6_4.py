manka = int(input())
ovsyanka = int(input())
man = set()
ovs = set()

for i in range(manka):
    man.add(input())

for j in range(ovsyanka):
    ovs.add(input())

vsego = man & ovs
if len(vsego) == 0:
    print("Таких нет")
else:
    print(len(vsego))
