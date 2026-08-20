def get_formatter(sep=" ", end=""):
    def formatter(*args):
        return sep.join(map(str, args)) + end

    return formatter


formatter = get_formatter()
print(formatter(1, 2, 3, 4, 5))