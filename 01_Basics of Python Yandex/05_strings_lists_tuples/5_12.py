kashas = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]
days = int(input())

for i in range(days):
    print(kashas[i % len(kashas)])
