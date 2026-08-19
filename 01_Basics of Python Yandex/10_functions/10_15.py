def get_dict(text):
    result_dict = {}

    pairs = text.split(";")
    for pair in pairs:
        key, value = pair.split("=")
        result_dict[key] = value
    return result_dict


result = get_dict("a=A;b=2;c=-3.5")
print(result)
