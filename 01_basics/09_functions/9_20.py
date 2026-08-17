def int_to_roman(num):
    # Словарь: число -> римское представление
    roman_dict = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }

    result = []
    for value, numeral in roman_dict.items():
        # Пока число больше или равно значению, добавляем римскую цифру
        while num >= value:
            result.append(numeral)
            num -= value
    return "".join(result)


def roman(a, b):
    summa = a + b
    return f"{int_to_roman(a)} + {int_to_roman(b)} = {int_to_roman(summa)}"


result = roman(10, 9)
print(result)
