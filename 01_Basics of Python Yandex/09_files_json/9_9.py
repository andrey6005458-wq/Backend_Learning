first = input()
second = input()
result = []

with open(first, "r", encoding="cp1251") as f:
    for line in f:
        line = line.strip()
        if line != "":
            cleaned = " ".join(line.split())
            result.append(cleaned + "\n")

with open(second, "w", encoding="utf-8") as f:
    f.writelines(result)
