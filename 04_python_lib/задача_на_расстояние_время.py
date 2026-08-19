magaz = int(input())
sklad = int(input())
speed = int(input())

range = (sklad - magaz) or (magaz - sklad)
time = float(range / speed)
print(f"{time:.2f}")