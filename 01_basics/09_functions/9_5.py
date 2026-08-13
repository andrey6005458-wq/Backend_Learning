__count = 0


def click():
    global __count
    __count += 1


def get_count():
    return __count


print(get_count())
click()
click()
click()
print(get_count())
