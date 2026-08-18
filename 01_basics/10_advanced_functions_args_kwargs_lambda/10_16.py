def login(name, password, success, error):
    total = sum(ord(ch) for ch in name)
    val = total * len(name)
    hex_str = f"{val:x}"
    if hex_str[::-1].lower() == password.lower():
        success(name)
    else:
        error(name)


def hello(username):
    print(f"Здравствуйте, {username}!")


def alert(username):
    print(f"!!! Попытка взлома аккаунта {username} !!!")
    print("Блокировка системы через...", 5, 4, 3, 2, 1, "ТРЕВОГА!", sep="\n")


login("оченьМаленькийРозовыйПони", "EDE5A", hello, alert)
