import csv
from datetime import datetime

# Получаем входные данные
user_id, class_id = input().split()

# Читаем необходимые файлы
with open("test.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # Пропускаем заголовок
    tests = list(reader)
with open("class_user_link.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # Пропускаем заголовок
    class_user_links = list(reader)
with open("test_class_user_link.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # Пропускаем заголовок
    test_class_user_links = list(reader)
with open("test_attempt.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # Пропускаем заголовок
    test_attempts = list(reader)

# Создаём словарь для быстрого доступа к тестам по id
test_dict = {test[0]: test[1] for test in tests}

# Находим связь между пользователем и классом
class_user_link_ids = []
for link in class_user_links:
    if link[2] == user_id and link[1] == class_id:
        class_user_link_ids.append(link[0])

# Список для назначенных тестов
assigned_tests = []
completed_tests = 0
# Для каждой связи ищем назначенные тесты
for class_user_link_id in class_user_link_ids:
    for link in test_class_user_links:
        if link[2] == class_user_link_id:
            test_id = link[1]
            test_class_user_link_id = link[0]
            datetime_started = datetime.strptime(link[3], "%d.%m.%Y %H:%M:%S")

            # Получаем название теста
            test_name = test_dict.get(test_id, "Unknown Test")

            # Проверяем, пройден ли тест
            test_completed = "FALSE"
            for attempt in test_attempts:
                if attempt[1] == test_class_user_link_id and attempt[2] == "TRUE":
                    test_completed = attempt[2]
                    completed_tests += 1
                    break

            data = {
                "test_name": test_name,
                "datetime_started": datetime_started,
                "test_completed": test_completed,
            }
            for i, assigned_test in enumerate(assigned_tests):
                if assigned_test["datetime_started"] < data["datetime_started"] or (
                    assigned_test["datetime_started"] == data["datetime_started"]
                    and assigned_test["test_name"] > data["test_name"]
                ):
                    assigned_tests.insert(i, data)
                    break
            else:
                assigned_tests.append(data)

print(f"{completed_tests}/{len(assigned_tests)}")

# Выводим информацию о каждом тесте
for test in assigned_tests:
    print(
        f"{test['test_name']} {test['datetime_started'].strftime('%d.%m.%y')} {test['test_completed']}"
    )
