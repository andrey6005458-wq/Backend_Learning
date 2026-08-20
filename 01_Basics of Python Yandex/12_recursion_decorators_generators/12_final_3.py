import json
from collections import defaultdict

# Чтение файла логов
with open("app.log", "r", encoding="utf-8") as f:
    logs = f.readlines()

# Сбор данных
users = set()
task_attempts = defaultdict(int)

for line in logs:
    line = line.strip()
    if not line:
        continue

    try:
        log_entry = json.loads(line)
        # Проверяем, что это попытка решения задачи
        if log_entry.get("handler") == "attempt_handler":
            params = log_entry.get("params", {})
            name = params.get("name")
            task = params.get("task")

            if name and task:
                users.add(name)
                task_attempts[task] += 1
    except json.JSONDecodeError:
        # Пропускаем некорректные строки
        continue

# Сортировка пользователей
sorted_users = sorted(users)

# Сортировка задач по названию
sorted_tasks = sorted(task_attempts.keys())
task_popularity = {task: task_attempts[task] for task in sorted_tasks}

# Находим самую популярную задачу
most_popular_task = max(task_attempts, key=task_attempts.get)
most_popular_count = task_attempts[most_popular_task]

# Вывод результатов
print("Analytics Results:")
print(f"Unique users who solved tasks: {len(users)}")
print(f"Unique users list: {', '.join(sorted_users)}")
print(f"Task popularity: {task_popularity}")
print(f"Most popular task: '{most_popular_task}' with {most_popular_count} attempts")
