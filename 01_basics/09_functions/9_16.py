def is_palindrome(x):

    if isinstance(x, str):
        items = list(x)
    elif isinstance(x, (int, float)):
        items = list(str(x))
    else:
        items = list(x)

    return items == items[::-1]


result = is_palindrome(123)
print(result)

result = is_palindrome([1, 2, 1, 2, 1])
print(result)
