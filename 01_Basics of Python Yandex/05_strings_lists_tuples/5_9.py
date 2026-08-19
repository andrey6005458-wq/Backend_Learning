while (text := input()) != "":
    if text.startswith("#"):
        continue
    elif (index := text.find("#")) != -1:
        print(text[:index])
    else:
        print(text)
