def secret_replace(text, **kwargs):
    counters = {}
    result = []

    for char in text:
        if char in kwargs:
            replacements = kwargs[char]
            if char not in counters:
                counters[char] = 0
            current_index = counters[char]
            result.append(replacements[current_index])
            counters[char] = (current_index + 1) % len(replacements)
        else:
            result.append(char)

    return "".join(result)


print(secret_replace("Hello, world!", l=("hi", "y"), o=("123", "z")))
