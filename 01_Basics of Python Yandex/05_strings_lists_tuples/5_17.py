text = input()
text = text.lower()
text_new = text.replace(" ", "")
polindrom = text_new[::-1]
if text_new == polindrom:
    print("YES")
else:
    print("NO")
