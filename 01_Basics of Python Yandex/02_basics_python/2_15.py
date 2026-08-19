num1 = int(input())
num2 = int(input())

a1 = num1 // 10 % 10
a2 = num1 % 10

b1 = num2 // 10 % 10
b2 = num2 % 10

numbers = [a1, a2, b1, b2]
max_val = max(numbers)
min_val = min(numbers)

mid_val = sum(numbers) - max_val - min_val
if mid_val >= 10:
    mid_val = mid_val % 10
else:
    mid_val == mid_val

print(f"{max_val}{mid_val}{min_val}")
