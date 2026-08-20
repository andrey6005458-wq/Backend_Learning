import csv
from datetime import datetime

# Получаем входные данные
user_id, class_id = input().split()

# Читаем необходимые файлы
with open("class_user_link.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # Пропускаем заголовок
    class_user_links = list(reader)
with open("test_class_user_link.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # Пропускаем заголовок
    test_class_user_links = list(reader)
with open("test_task_link.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # Пропускаем заголовок
    test_task_links = list(reader)
with open("task_attempt.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # Пропускаем заголовок
    task_attempts = list(reader)
with open("task_attempt.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # Пропускаем заголовок
    task_attempts = list(reader)
with open("test_attempt.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # Пропускаем заголовок
    test_attempts = list(reader)
with open("task.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # Пропускаем заголовок
    tasks = list(reader)

task_dict = {task[0]: task for task in tasks}

# Находим связь между пользователем и классом
for link in class_user_links:
    if link[2] == user_id and link[1] == class_id:
        class_user_link_id = link[0]
        break


# Находим все тесты для данного пользователя, отсортированные по дате
user_tests = []
for link in test_class_user_links:
    if link[2] == class_user_link_id:
        test_id = link[1]
        test_class_user_link_id = link[0]
        datetime_started = datetime.strptime(link[3], "%d.%m.%Y %H:%M:%S")
        data = {
            "test_id": test_id,
            "class_user_link_id": link[2],
            "test_class_user_link_id": test_class_user_link_id,
            "datetime_started": datetime_started,
        }
        # Сортируем тесты по дате выдачи (от поздних к ранним)
        for i, user_test in enumerate(user_tests):
            if user_test["datetime_started"] < data["datetime_started"]:
                user_tests.insert(i, data)
                break
        else:
            user_tests.append(data)

if not user_tests:
    print("Тестов не найдено")
    exit()

latest_test = user_tests[0]
test_id = latest_test["test_id"]
test_class_user_link_id = latest_test["test_class_user_link_id"]
for test_attempt in test_attempts:
    if test_attempt[1] == test_class_user_link_id:
        test_attempt_id = test_attempt[0]
        break
else:
    print("Попытки не найдено")
    exit()

# Получаем все задачи для этого теста
test_tasks = []
for link in test_task_links:
    if link[1] == test_id:
        data = {
            "order_number": int(link[3]),
            "task_id": link[2],
        }
        # Сортируем задачи по порядковому номеру
        for i, test_task in enumerate(test_tasks):
            if test_task["order_number"] > data["order_number"]:
                test_tasks.insert(i, data)
                break
        else:
            test_tasks.append(data)

# Получаем ответы для задач
task_results = {}
total_time_spent_seconds = 0

for attempt in task_attempts:
    if attempt[2] == test_attempt_id:
        task_id = attempt[1]
        user_answer = attempt[3]

        if user_answer.strip() == "":
            continue  # Пропускаем, если ответ пустой

        is_correct = attempt[3] == task_dict[task_id][2]
        time_spent = int(attempt[5]) if attempt[5] else 0  # Время в секундах
        total_time_spent_seconds += int(time_spent)

        # Добавляем результат задачи
        task_results[task_id] = {
            "is_correct": is_correct,
            "time_spent": time_spent,
        }

# Вычисляем проценты
total_questions = len(test_tasks)
answered_questions = len(task_results)
correct_answers = sum(1 for result in task_results.values() if result["is_correct"])
percentage_answered = (
    (answered_questions / total_questions * 100) if total_questions > 0 else 0
)
percentage_correct = (
    (correct_answers / answered_questions * 100) if answered_questions > 0 else 0
)

# Выводим результаты
print(f"{percentage_answered:.1f}% {percentage_correct:.1f}%")

for task in test_tasks:
    task_id = task["task_id"]

    # Определяем статус ответа
    if task_id in task_results:
        answer_status = "TRUE" if task_results[task_id]["is_correct"] else "FALSE"
    else:
        answer_status = "?"

    print(f"{task['order_number']} {answer_status} {task_id}")

# Формируем время в формате hh:mm:ss
hours, remainder = divmod(total_time_spent_seconds, 3600)
minutes, seconds = divmod(remainder, 60)
print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
