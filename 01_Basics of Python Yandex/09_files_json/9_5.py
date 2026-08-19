from sys import stdin

polindrom = set()
for line in stdin:
    for word in line.split():
        if word.lower() == word.lower()[::-1]:
            polindrom.add(word)

polindrom = sorted(polindrom)
print(*polindrom, sep="\n")
