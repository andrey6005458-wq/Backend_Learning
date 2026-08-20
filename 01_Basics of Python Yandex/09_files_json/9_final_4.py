import csv
import json
from datetime import datetime

# Чтение входных данных
user_id, class_id = input().split()

# Чтение данных из CSV-файлов
with open("user.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # Пропускаем заголовок
    users = list(reader)
with open("class_user_link.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # Пропускаем заголовок
    class_user_links = list(reader)
with open("task.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # Пропускаем заголовок
    tasks = list(reader)
with open("test.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # Пропускаем заголовок
    tests = list(reader)
with open("test_task_link.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # Пропускаем заголовок
    test_task_links = list(reader)
with open("test_class_user_link.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # Пропускаем заголовок
    test_class_user_links = list(reader)
with open("test_attempt.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # Пропускаем заголовок
    test_attempts = list(reader)
with open("task_attempt.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # Пропускаем заголовок
    task_attempts = list(reader)

users_dict = {user[0]: user for user in users}
class_user_links_dict = {
    (class_user_link[1], class_user_link[2]): class_user_link
    for class_user_link in class_user_links
}
tasks_dict = {task[0]: task for task in tasks}
tests_dict = {test[0]: test for test in tests}
test_attempts_dict = {test_attempt[1]: test_attempt for test_attempt in test_attempts}
task_attempts_dict = {
    (task_attempt[1], task_attempt[2]): task_attempt for task_attempt in task_attempts
}

if user_id not in users_dict:
    print("Пользователь не найден")
    exit()

# Проверка принадлежности пользователя к классу
class_user_link = class_user_links_dict.get((class_id, user_id), None)
if not class_user_link:
    print("Пользователь не принадлежит к указанному классу")
    exit()

# Формирование информации о пользователе
user_info = {
    "user_id": int(user_id),
    "full_name": f"{users_dict[user_id][4]} {users_dict[user_id][2]}",  # last_name, first_name
    "class_id": int(class_id),
}

# Получение списка тестов, выданных пользователю
user_test_links = []
for link in test_class_user_links:
    if link[2] == class_user_link[0]:
        link[3] = datetime.strptime(link[3], "%d.%m.%Y %H:%M:%S")
        for i, user_test_link in enumerate(user_test_links):
            if link[3] > user_test_link[3]:
                user_test_links.insert(i, link)
                break
        else:
            user_test_links.append(link)

# Формирование списка тестов с задачами и статусом их выполнения
tests_data = []
accuracy_sum = 0
test_count = 0
tests_completed = 0

for test_link in user_test_links:
    test_id = test_link[1]

    test_info = tests_dict.get(test_id, None)
    if test_info is None:
        print("Тест не найден")
        continue

    test_attempt = test_attempts_dict.get(test_link[0], None)

    # Получение задач теста
    test_tasks = []
    for link in test_task_links:
        if link[1] == test_id:
            for i, test_task in enumerate(test_tasks):
                if int(link[3]) < int(test_task[3]):
                    test_tasks.insert(i, link)
                    break
            else:
                test_tasks.append(link)

    tasks_data = []
    correct_count = 0
    answered_count = 0
    total_time_seconds = 0

    for task_link in test_tasks:
        task_id = task_link[2]  # task_id

        # Получение статуса выполнения задачи
        task_attempt = task_attempts_dict.get((task_id, test_attempt[0]), None)

        is_correct = "?"
        if task_attempt:
            user_answer = task_attempt[3].strip()
            if user_answer != "":
                answered_count += 1
                # Получение правильного ответа для задачи
                task_info = tasks_dict.get(task_id, None)

                if task_info:
                    if task_attempt[3] == task_info[2]:
                        correct_count += 1
                        is_correct = "TRUE"
                    else:
                        is_correct = "FALSE"

            # Учёт времени выполнения
            if task_attempt[5]:  # time_spent
                total_time_seconds += int(task_attempt[5])

        tasks_data.append(
            {
                "order_number": int(task_link[3]),  # order_number
                "task_id": int(task_id),
                "is_correct": is_correct,
            }
        )

    # Расчёт процента выполнения и точности
    total_tasks = len(test_tasks)
    progress_percent = 100.0 * answered_count / total_tasks if total_tasks > 0 else 0.0
    correct_percent = (
        100.0 * correct_count / answered_count if answered_count > 0 else 0.0
    )

    # Форматирование времени
    hours = total_time_seconds // 3600
    minutes = (total_time_seconds % 3600) // 60
    seconds = total_time_seconds % 60

    # Добавление информации о тесте
    test_data = {
        "test_id": int(test_id),
        "title": test_info[1],
        "tasks": tasks_data,
        "progress_percent": round(progress_percent, 1),
        "correct_percent": round(correct_percent, 1),
        "time": f"{hours:02d}:{minutes:02d}:{seconds:02d}",
        "date_assigned": test_link[3].strftime("%d.%m.%y"),
    }

    tests_data.append(test_data)

    if test_attempt and test_attempt[2] == "TRUE":
        tests_completed += 1
    # Учёт точности для расчёта среднего
    if answered_count > 0:
        accuracy_sum += correct_percent
        test_count += 1

# Расчёт общего прогресса
accuracy_average = accuracy_sum / test_count if test_count > 0 else 0

progress_info = {
    "tests_completed": tests_completed,
    "tests_total": len(tests_data),
    "accuracy_average_percent": round(accuracy_average, 1),
}

# Формирование итогового словаря
result = {"user": user_info, "progress": progress_info, "tests": tests_data}

# Вывод результата
print(json.dumps(result, ensure_ascii=False, indent=2))
