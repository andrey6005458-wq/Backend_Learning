string = "Российская Федерация"
answer = "".join(word[0] for word in string.split()).upper()
print(answer)
