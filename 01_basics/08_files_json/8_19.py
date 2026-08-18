shift = int(input())
a = "abcdefghijklmnopqrstuvwxyz"
with open("public.txt", "r", encoding="UTF-8") as file_in:
    data = file_in.read()
data_out = [
    a[(a.find(i.lower()) + shift) % len(a)] if i.lower() in a else i for i in data
]
for ind, letter in enumerate(data):
    if letter.isupper():
        data_out[ind] = data_out[ind].upper()
with open("private.txt", "w") as file_out:
    print("".join(data_out), file=file_out)
