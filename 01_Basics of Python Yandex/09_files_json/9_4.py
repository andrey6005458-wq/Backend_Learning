from sys import stdin

lines = [line.strip() for line in stdin]
for line in lines[:-1]:
    if lines[-1].lower() in line.lower():
        print(line)
