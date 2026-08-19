count = 0
n = int(input())

for i in range(n):
    has_zayka = False
    while True:
        text = input()
        if text == "ВСЁ":
            break
        if text == "зайка":
            has_zayka = True
    if has_zayka:
        count += 1

print(count)
