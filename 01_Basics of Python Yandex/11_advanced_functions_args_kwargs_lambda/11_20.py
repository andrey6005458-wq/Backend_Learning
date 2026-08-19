from datetime import datetime

data_base = []


def insert(*users):
    for user in users:
        data_base.append(user)


def select(*conditions):
    # Если условий нет — возвращаем всех, отсортированных по id
    if not conditions:
        return sorted(data_base, key=lambda u: u["id"])

    # Фильтруем по каждому условию
    filtered = data_base[:]
    for cond in conditions:
        # Разбираем условие
        parts = cond.split()
        if len(parts) != 3:
            continue
        field, op, value = parts

        # Приводим значение к правильному типу
        if field == "id":
            value = int(value)
        elif field == "birth":
            value = datetime.strptime(value, "%d.%m.%Y")
            # Для сравнения дат в цикле преобразуем user[field]
            # Ниже будем преобразовывать каждую дату при сравнении

        # Фильтруем
        filtered = [u for u in filtered if matches(u, field, op, value)]

    return sorted(filtered, key=lambda u: u["id"])


def matches(user, field, op, value):
    user_val = user[field]

    # Преобразуем дату, если нужно
    if field == "birth":
        user_val = datetime.strptime(user_val, "%d.%m.%Y")

    # Сравниваем
    if op == "==":
        return user_val == value
    elif op == "!=":
        return user_val != value
    elif op == ">":
        return user_val > value
    elif op == "<":
        return user_val < value
    elif op == ">=":
        return user_val >= value
    elif op == "<=":
        return user_val <= value
    else:
        return False


insert({"id": 1, "name": "Ann", "birth": "01.03.2001"})
insert(
    {"id": 3, "name": "Bob", "birth": "05.03.2002"},
    {"id": 4, "name": "Chuck", "birth": "07.06.2001"},
)
print([user["name"] for user in select()])
print([user["name"] for user in select("name > B")])
insert({"id": 2, "name": "Den", "birth": "29.02.2000"})
print([user["name"] for user in select("name > B")])
print([user["name"] for user in select("id <= 2")])
print(*select("birth >= 12.04.2001"), sep="\n")
