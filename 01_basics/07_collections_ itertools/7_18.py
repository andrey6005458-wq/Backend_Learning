from itertools import product

statement = input()
print("a b c f")
table = product([0, 1], repeat=3)
for row in table:
    res = {"a": row[0], "b": row[1], "c": row[2]}
    print(res["a"], res["b"], res["c"], int(eval(statement, res)))
