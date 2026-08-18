def choice(*args, **kwargs):
    if "min" in kwargs:
        func = kwargs["min"]
        return min(func(x) for x in args)
    elif "max" in kwargs:
        func = kwargs["max"]
        return max(func(x) for x in args)


result = choice(321, 87, 1000, -23, min=lambda x: len(str(x)))
print(result)
