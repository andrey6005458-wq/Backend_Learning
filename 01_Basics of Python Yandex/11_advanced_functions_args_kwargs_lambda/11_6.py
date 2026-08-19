def get_operator(x):
    if x == "+":
        return lambda a, b: a + b
    elif x == "-":
        return lambda a, b: a - b
    elif x == "*":
        return lambda a, b: a * b
    elif x == "/":
        return lambda a, b: a / b
    elif x == "//":
        return lambda a, b: a // b
    elif x == "%":
        return lambda a, b: a % b
    elif x == "**":
        return lambda a, b: a**b
    else:
        return None


operator_power = get_operator("**")
print(operator_power(2, 10))
