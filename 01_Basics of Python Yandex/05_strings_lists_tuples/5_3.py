string_length = int(input())
number_of_rows = int(input())

for i in range(number_of_rows):
    text = input()
    if len(text) > string_length:
        print(text[: string_length - 3] + "...")
    else:
        print(text)
