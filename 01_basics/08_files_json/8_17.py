with open("secret.txt", "r", encoding="UTF-8") as f:
    print("".join([chr(ord(i) % 128) for i in f.read()]))
