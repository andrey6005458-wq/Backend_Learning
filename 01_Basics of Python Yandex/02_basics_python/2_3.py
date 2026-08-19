speed1 = int(input())
speed2 = int(input())
speed3 = int(input())

if speed1 > speed2 and speed1 > speed3:
    print("Петя")
elif speed2 > speed1 and speed2 > speed3:
    print("Вася")
else:
    print("Толя")