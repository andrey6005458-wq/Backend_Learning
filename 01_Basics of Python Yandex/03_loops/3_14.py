number = int(input())

if number < 2:
    print("NO")
else:
    count = 0
    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            count += 1

    if count == 0:
        print("YES")
    else:
        print("NO")
