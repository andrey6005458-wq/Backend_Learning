from sys import stdin

sum_rost = 0
sum_kids = 0

for line in stdin:
    a, b = map(int, line.split()[1:])
    sum_rost += b - a
    sum_kids += 1

print(round(sum_rost / sum_kids))
