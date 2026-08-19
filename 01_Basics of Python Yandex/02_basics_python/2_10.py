namber = int(input())
a = namber // 100
b = (namber // 10) % 10
c = namber % 10

num1 = b + c
num2 = a + b

if num1 > num2:
    print(f"{num1}{num2}")
else:
    print(f"{num2}{num1}")
