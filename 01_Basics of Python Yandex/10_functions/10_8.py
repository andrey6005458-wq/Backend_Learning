def fragments(numbers):
    if not numbers:
        return []

    result = []
    current = [numbers[0]]

    for num in numbers[1:]:
        if num > current[-1]:
            current.append(num)
        else:
            result.append(current)
            current = [num]

    result.append(current)
    return result


result = fragments([-4, -2, 5, 0, 3, 7, -8, -2, 6, 7, 6, 8, 10, 5, 7, 8])
print(result)
