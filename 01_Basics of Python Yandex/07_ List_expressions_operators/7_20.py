text = "ехали медведи на велосипеде"
answer = {
    tuple(sorted((w1, w2)))
    for i, w1 in enumerate(text.split())
    for w2 in text.split()[i + 1 :]
    if len(set(w1) & set(w2)) >= 3
}
print(answer)
