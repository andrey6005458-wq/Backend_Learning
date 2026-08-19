result = 0
while price := float(input()):
    if price >= 500:
        price *= 0.9
    result += price
print(f"{result:.1f}")
