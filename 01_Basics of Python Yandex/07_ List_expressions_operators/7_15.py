text = """Ехали медведи
На велосипеде.

А за ними кот
Задом наперёд."""
answer = {
    ch.lower(): text.lower().count(ch.lower()) for ch in set(text) if ch.isalpha()
}
print(answer)
