__data = []


def enter_results(*args):
    global __data
    __data += args


def get_sum():
    return round(sum(__data[::2]), 2), round(sum(__data[1::2]), 2)


def get_average():
    return round(2 * get_sum()[0] / len(__data), 2), round(
        2 * get_sum()[1] / len(__data), 2
    )


enter_results(1, 2, 3, 4, 5, 6)
print(get_sum(), get_average())
enter_results(1, 2)
print(get_sum(), get_average())
