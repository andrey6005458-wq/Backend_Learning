side = int(input())
a, b = map(int,input().split())

plitka = side * side
pole = a * b
answer = pole / plitka 
print(f'{int(answer)}')