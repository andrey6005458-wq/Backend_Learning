# Считываем параметры курса
(
    num_students,
    num_lessons,
    max_rating,
    classwork_coefficient,
    selfwork_coefficient,
    homework_coefficient,
    testwork_coefficient,
) = map(int, input().split())

# Проверяем корректность параметров
if (
    num_lessons > 0
    and classwork_coefficient > 0
    and selfwork_coefficient > 0
    and homework_coefficient > 0
    and testwork_coefficient > 0
):
    student_lastname = input().strip()  # фамилия ученика

    # Инициализация сумм оценок
    classwork_sum = 0
    selfwork_sum = 0
    homework_sum = 0
    testwork_sum = 0

    # Считываем M строк с оценками
    for _ in range(num_lessons):
        classwork, selfwork, homework, testwork = map(int, input().split(","))
        classwork_sum += classwork
        selfwork_sum += selfwork
        homework_sum += homework
        testwork_sum += testwork

    # Рассчитываем рейтинг
    rating = (
        classwork_sum * classwork_coefficient
        + selfwork_sum * selfwork_coefficient
        + homework_sum * homework_coefficient
        + testwork_sum * testwork_coefficient
    )

    # Проверяем, не превышает ли рейтинг максимальный
    if rating > max_rating:
        print("Во введённых данных ошибка")
    else:
        percent = round(rating * 100 / max_rating)
        print(f"{student_lastname} {percent}%")
else:
    print("Во введённых данных ошибка")
