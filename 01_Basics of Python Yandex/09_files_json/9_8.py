first = input()
second = input()
answer = input()

with open(first, "r") as f:
    first_set = set(f.read().split())

with open(second, "r") as f:
    second_set = set(f.read().split())

result = sorted(first_set ^ second_set)

with open(answer, "w") as f:
    f.write("\n".join(result))
