count = 0
word_count = int(input())
for i in range(word_count):
    text = input()
    if text[0] in "абв":
        count += 1
if count == word_count:
    print("YES")
else:
    print("NO")
