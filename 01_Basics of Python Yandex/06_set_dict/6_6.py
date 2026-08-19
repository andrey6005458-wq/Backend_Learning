n = int(input())
m = int(input())

n_k = set()
m_k = set()

for i in range(n + m):
    if (x := input()) in n_k:
        m_k.add(x)
    else:
        n_k.add(x)

k = n_k ^ m_k
if len(k) == 0:
    print("Таких нет")
else:
    k = sorted(list(k))
    print(*k, sep="\n")
