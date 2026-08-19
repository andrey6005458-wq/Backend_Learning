def make_equation(*coeffs):
    if len(coeffs) == 1:
        return str(coeffs[0])
    *rest, last = coeffs
    return "(" + make_equation(*rest) + ") * x + " + str(last)


result = make_equation(3, 1, 5, 3)
print(result)
