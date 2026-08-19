name = input()
locker_number = int(input())
group_number = locker_number // 100
bed_number = (locker_number // 10) % 10
sequence_number = locker_number % 10
print(f"Группа №{group_number}.")
print(f"{sequence_number}. {name}.")
print(f"Шкафчик: {locker_number}.")
print(f"Кроватка: {bed_number}.")
