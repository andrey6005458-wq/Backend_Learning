print(
    dict(
        map(
            lambda item: (
                "".join(ch for ch in item[0].lower() if ch.isalpha()),
                (
                    sum(item[1])
                    if hasattr(item[1], "__iter__")
                    and not isinstance(item[1], (str, bytes))
                    else item[1]
                ),
            ),
            {"First 1": 2, "second:": (2, 1, 1), "THIRD": [1, 2, 3]}.items(),
        )
    )
)
