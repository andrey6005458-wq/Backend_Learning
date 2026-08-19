number = int(input())
x = 0
old_number = number
while old_number > 0:
    x *= 10
    x += old_number % 10
    old_number //= 10
if x == number:
    print("YES")
else:
    print("NO")
