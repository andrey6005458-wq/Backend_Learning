n = int(input())
rows = []
current = 1
count_in_row = 1

while current <= n:
    row_numbers = []
    for i in range(count_in_row):
        if current <= n:
            row_numbers.append(str(current))
            current += 1
        else:
            break
    rows.append(" ".join(row_numbers))
    count_in_row += 1

width = len(rows[-1])

for row in rows:
    print(f"{row:^{width}}")
