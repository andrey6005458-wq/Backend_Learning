words = "Ехали медведи на велосипеде"
answer = [
    word
    for word in words.split()
    if sum(glassn.lower() in "аяуюоёэеиыaeiouy" for glassn in word) >= 3
]
print(answer)
