low = 1
high = 1000

while True:
    mid = (low + high) // 2
    print(mid)
    answer = input()

    if answer == "Угадал!":
        break
    elif answer == "Больше":
        low = mid + 1
    elif answer == "Меньше":
        high = mid - 1
