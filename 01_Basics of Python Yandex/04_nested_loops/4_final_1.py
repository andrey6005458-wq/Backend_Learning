(
    num_students,
    num_lessons,
    max_rating,
    classwork_coefficient,
    selfwork_coefficient,
    homework_coefficient,
    testwork_coefficient,
) = map(int, input().split())

print(f"""{num_lessons}
{num_students}
{classwork_coefficient}
{selfwork_coefficient}
{homework_coefficient}
{testwork_coefficient}
{max_rating}""")
