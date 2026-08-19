a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c:
    hip = a
    kat1, kat2 = b, c
elif b >= a and b >= c:
    hip = b
    kat1, kat2 = a, c
else:
    hip = c
    kat1, kat2 = b, a

if kat1**2 + kat2**2 == hip**2:
    print("100%")
elif kat1**2 + kat2**2 < hip**2:
    print("велика")
else:
    print("крайне мала")
