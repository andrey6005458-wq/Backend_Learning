a = int(input())
b = int(input())
c = int(input())

num1 = a // 10
num2 = a % 10

num3 = b // 10
num4 = b % 10

num5 = c // 10
num6 = c % 10

if num1 == num3 == num5:
    print(num1)
elif num2 == num4 == num6:
    print(num2)
