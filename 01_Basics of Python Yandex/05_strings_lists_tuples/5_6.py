count = 0
place = int(input())

for i in range(place):
    text = input()
    count += text.count("зайка")
print(count)
