line = input()
temp_line, repeat = line[0], 1
for i in line[1:]:
    if i == temp_line:
        repeat += 1
    else:
        print(temp_line, repeat)
        temp_line, repeat = i, 1
print(temp_line, repeat)
