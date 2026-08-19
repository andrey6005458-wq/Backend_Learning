from itertools import accumulate

words = [word + " " for word in input().split()]
for text in accumulate(words):
    print(text)
