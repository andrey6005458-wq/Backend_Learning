print(
    dict(
        filter(
            lambda item: isinstance(item[1], list)
            and any(isinstance(x, int) and x % 2 == 0 for x in item[1]),
            {"first": [7, 2, "1"], "second": (45, 2, 14), "third": [98]}.items(),
        )
    )
)
