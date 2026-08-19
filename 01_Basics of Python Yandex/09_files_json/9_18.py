import os

size = os.path.getsize(input())
if size > 1024**3 - 1:
    size = int(size / 1024**3) + 1
    postfix = "ГБ"
elif size > 1024**2 - 1:
    size = int(size / 1024**2) + 1
    postfix = "МБ"
elif size > 1023:
    size = int(size / 1024) + 1
    postfix = "КБ"
else:
    postfix = "Б"
print(str(size) + postfix)
