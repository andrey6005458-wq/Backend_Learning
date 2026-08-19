def convert_from_base_to_base(num, from_base=10, to_base=10):
    n = int(num, from_base) if isinstance(num, str) else num
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while n > 0:
        n, m = divmod(n, to_base)
        result += alphabet[m]
    return result[::-1]


number = input()
max_benefit, best_base = 0, 0
for base in range(2, 11):
    if (
        digits_sum := sum(map(int, convert_from_base_to_base(number, 10, base)))
    ) > max_benefit:
        best_base = base
        max_benefit = digits_sum
print(best_base)
