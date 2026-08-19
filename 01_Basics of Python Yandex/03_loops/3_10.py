step = input()
x = 0
y = 0

while step != "СТОП":
    k = int(input())
    if step == "СЕВЕР":
        y += k
    elif step == "ЮГ":
        y -= k
    elif step == "ВОСТОК":
        x += k
    else:
        x -= k
    step = input()
print(y)
print(x)
