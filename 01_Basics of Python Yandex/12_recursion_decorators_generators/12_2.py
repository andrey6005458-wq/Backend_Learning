from functools import lru_cache


@lru_cache(maxsize=None)
def recursive_digit_sum(numbers):
    if not numbers:
        return 0
    return recursive_digit_sum(numbers // 10) + numbers % 10


result = recursive_digit_sum(7321346)
print(result)
