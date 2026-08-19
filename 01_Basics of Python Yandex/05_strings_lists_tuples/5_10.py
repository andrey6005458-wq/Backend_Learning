letters = []
counts = []

while (text := input()) != "ФИНИШ":
    text = text.lower()
    for char in text:
        if char == " ":
            continue
        if char in letters:
            index = letters.index(char)
            counts[index] += 1
        else:
            letters.append(char)
            counts.append(1)

max_count = max(counts)
result = []
for i in range(len(letters)):
    if counts[i] == max_count:
        result.append(letters[i])

print(min(result))
