answer = set()
while (text := input()) != "":
    forest = [x.strip() for x in text.split()]
    for i in range(len(forest)):
        if forest[i] == "зайка":
            if i - 1 >= 0:
                answer.add(forest[i - 1])
            if i + 1 < len(forest):
                answer.add(forest[i + 1])
print(*answer, sep="\n")
