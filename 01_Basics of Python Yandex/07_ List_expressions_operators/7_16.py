rle = [("a", 2), ("b", 3), ("c", 1)]
answer = "".join([ch * count for ch, count in rle])
print(answer)
