pet = int(input())
vas = int(input())
tol = int(input())

if pet > vas and vas > tol:
    first, second, third = "Петя", "Вася", "Толя"
elif pet > tol and tol > vas:
    first, second, third = "Петя", "Толя", "Вася"
elif vas > pet and pet > tol:
    first, second, third = "Вася", "Петя", "Толя"
elif vas > tol and tol > pet:
    first, second, third = "Вася", "Толя", "Петя"
elif tol > pet and pet > vas:
    first, second, third = "Толя", "Петя", "Вася"
else:
    first, second, third = "Толя", "Вася", "Петя"

print(f'{"": ^8}{first: ^8}{"": ^8}')
print(f'{second: ^8}{"": ^8}{"": ^8}')
print(f'{"": ^8}{"": ^8}{third: ^8}')
print(f'{"II": ^8}{"I": ^8}{"III": ^8}')
