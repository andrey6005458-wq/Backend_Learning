numbers = {1, 2, 3, 4, 5}
answer = {
    num
    for num in numbers
    if num > 1 and all(num % div != 0 for div in range(2, int(num**0.5) + 1))
}
print(answer)
