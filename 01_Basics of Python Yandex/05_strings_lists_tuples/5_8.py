place = int(input())

for i in range(place):
    text = input()
    zayka = text.find("зайка") + 1
    if zayka == 0:
        print("Заек нет =(")
    else:
        print(zayka)
