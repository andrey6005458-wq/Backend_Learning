a = int(input())
b = int(input())
c = int(input())
free = (a + b + c) - 30
ost = 30 - (a + b + c)

if ost >= free:
    print("Да, всех животных можно разместить.")
    print(f"Останется свободных мест: {ost}")
else:
    print("Нет, всех животных разместить нельзя.")
    print(f"Не хватает мест: {free}")
