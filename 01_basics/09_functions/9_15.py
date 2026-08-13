def get_dict(text):
    result_dict = {}
    pairs = text.split(";")

    for pair in pairs:
        key, value = pair.split("=")
        result_dict[key] = value

    return result_dict


result = get_dict("id=3-76;ip=127.0.0.1;phone=+7-(123)-456-78-90")
print(result)
