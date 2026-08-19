def is_prime(x):
    if x < 2:
        return False
    else:
        count = 0
    for divisor in range(2, int(x**0.5) + 1):
        if x % divisor == 0:
            count += 1
    if count == 0:
        return True
    else:
        return False


result = is_prime(1001459)
print(result)

result = is_prime(79701)
print(result)
