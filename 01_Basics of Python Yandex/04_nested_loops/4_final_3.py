(
    num_students,
    num_lessons,
    max_rating,
    classwork_coefficient,
    selfwork_coefficient,
    homework_coefficient,
    testwork_coefficient,
) = map(
    int, input().split()
)  # Считываем параметры курса

# Проверяем корректность входных данных
if (
    num_students >= 3  # Минимум 3 ученика
    and num_lessons > 0  # Должно быть хотя бы одно занятие
    and classwork_coefficient > 0
    and selfwork_coefficient > 0
    and homework_coefficient > 0
    and testwork_coefficient > 0
    and max_rating > 0  # Максимальный рейтинг должен быть положительным
):
    # Инициализация переменных для поиска топ-3 учеников и расчёта рейтинга программы
    max_rating_abs = 0
    max_rating_abs2 = 0
    max_rating_abs3 = 0
    student1_lastname = None
    student2_lastname = None
    student3_lastname = None

    sum_rating_abs = 0
    min_rating_abs = max_rating

    # Обрабатываем данные по каждому ученику
    for _ in range(num_students):
        student_lastname = input()  # Считываем фамилию ученика

        # Инициализируем суммарные баллы за разные виды работ
        classwork_sum = 0
        homework_sum = 0
        selfwork_sum = 0
        testwork_sum = 0

        # Считываем оценки по каждому занятию
        for i in range(num_lessons):
            classwork, selfwork, homework, testwork = map(int, input().split(","))
            classwork_sum += classwork
            selfwork_sum += selfwork
            homework_sum += homework
            testwork_sum += testwork

        # Рассчитываем итоговый рейтинг ученика
        rating = (
            classwork_sum * classwork_coefficient
            + homework_sum * homework_coefficient
            + selfwork_sum * selfwork_coefficient
            + testwork_sum * testwork_coefficient
        )

        # Обновляем топ-3 учеников
        if rating > max_rating_abs:
            max_rating_abs3 = max_rating_abs2
            student3_lastname = student2_lastname
            max_rating_abs2 = max_rating_abs
            student2_lastname = student1_lastname
            max_rating_abs = rating
            student1_lastname = student_lastname
        elif rating > max_rating_abs2:
            max_rating_abs3 = max_rating_abs2
            student3_lastname = student2_lastname
            max_rating_abs2 = rating
            student2_lastname = student_lastname
        elif rating > max_rating_abs3:
            max_rating_abs3 = rating
            student3_lastname = student_lastname

        # Обновляем минимальный рейтинг
        if rating < min_rating_abs:
            min_rating_abs = rating
        sum_rating_abs += rating  # Добавляем рейтинг ученика в суммарный

    # Проверяем, не превышает ли максимальный рейтинг допустимое значение
    if max_rating_abs > max_rating:
        print("Во введённых данных ошибка")
    else:
        # Вычисляем максимальный, средний и минимальный рейтинг в процентах
        max_rating_perc = round(max_rating_abs * 100 / max_rating)
        avg_rating_perc = round((sum_rating_abs / num_students) * 100 / max_rating)
        min_rating_perc = round(min_rating_abs * 100 / max_rating)

        # Определяем, насколько хорошо усваивается курс
        if avg_rating_perc > 50:
            verdict = "Курс усваивается хорошо"
        else:
            verdict = "Курс усваивается плохо"

        # Выводим результаты
        print(f"""{max_rating_perc} {avg_rating_perc} {min_rating_perc}
{student1_lastname} {round(max_rating_abs * 100 / max_rating)}%
{student2_lastname} {round(max_rating_abs2 * 100 / max_rating)}%
{student3_lastname} {round(max_rating_abs3 * 100 / max_rating)}%
{verdict}
        """)
else:
    print("Во введённых данных ошибка")  # Ошибка при некорректных входных данных
