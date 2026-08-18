def product(*args, **kwargs):
    result = []
    for i in args:
        product_value = 1
        found = False
        for key, value in kwargs.items():
            if key in i:
                product_value *= value
                found = True
        if found:
            result.append(product_value)
    return tuple(result)


result = product("Ann", "Bob", "Chuck", a=9, n=5, u=3, c=2, A=5)
print(result)
