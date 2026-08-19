p = int(input())
v = int(input())
t = int(input())

if p > v and p > t:
    first = "Петя"
elif v > p and v > t:
    first = "Вася"
else:
    first = "Толя"

if p > v and p < t or p > t and p < v:
    second = "Петя"
elif v > p and v < t or v > t and v < p:
    second = "Вася"
else:
    second = "Толя"

if first == "Петя":
    if second == "Вася":
        third = "Толя"
    else:
        third = "Вася"
elif first == "Вася":
    if second == "Петя":
        third = "Толя"
    else:
        third = "Петя"
else:  
    if second == "Петя":
        third = "Вася"
    else:
        third = "Петя"

print("1.", first)
print("2.", second)
print("3.", third)