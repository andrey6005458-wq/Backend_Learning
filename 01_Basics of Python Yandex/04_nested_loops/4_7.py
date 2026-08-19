n = int(input())
time = 3

for i in range(n):
    next_time = time
    while next_time > 0:
        if next_time == 1:
            print(f"До старта {next_time} секунд(а)")
        else:
            print(f"До старта {next_time} секунд(ы)")
        next_time -= 1
    print(f"Старт {i + 1}!!!")
    time += 1
