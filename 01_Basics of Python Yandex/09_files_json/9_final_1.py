import csv

files = [
    "user.csv",
    "class.csv",
    "class_user_link.csv",
    "task.csv",
    "test.csv",
    "test_task_link.csv",
    "test_class_user_link.csv",
    "test_attempt.csv",
    "task_attempt.csv",
]

counts = []
for filename in files:
    with open(filename, "r") as f:
        reader = csv.reader(f)
        rows = list(reader)

        if rows:
            counts.append(len(rows) - 1)
        else:
            counts.append(0)

print(*counts)
