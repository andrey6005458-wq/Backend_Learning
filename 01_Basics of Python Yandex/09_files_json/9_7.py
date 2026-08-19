name = input()
numbers = []

with open(name, "r") as f:
    for line in f:
        for x in line.split():
            numbers.append(int(x))

total_count = len(numbers)
positive_count = len([x for x in numbers if x > 0])
total_sum = sum(numbers)

print(total_count)
print(positive_count)
print(min(numbers))
print(max(numbers))
print(total_sum)
print(round(total_sum / total_count, 2))
