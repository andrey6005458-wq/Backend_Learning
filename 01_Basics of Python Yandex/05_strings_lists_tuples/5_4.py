while (text := input()) != "":
    if text.endswith("@@"):
        continue
    if text.startswith("##"):
        text = text[2:]
    print(text)
