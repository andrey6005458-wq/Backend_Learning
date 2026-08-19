n = int(input())
wrong = -1
h_last = 0

for i in range(n):
    b = int(input())
    h = b % 256
    m = b // 256**2
    r = (b // 256) % 256
    h_curr = (37 * (m + r + h_last)) % 256
    if h_curr != h or h >= 100:
        wrong = i
        break
    h_last = h
print(wrong)
