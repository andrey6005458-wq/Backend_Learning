a, b = map(int, input().split())
slise = a * 8
every = slise // b
ostatot = slise % b
print(f'{every} {ostatot}')