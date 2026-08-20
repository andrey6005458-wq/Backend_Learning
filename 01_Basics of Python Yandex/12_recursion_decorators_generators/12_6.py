def merge_sort(arr):
    # Базовый случай: если список пуст или из одного элемента — он уже отсортирован
    if len(arr) <= 1:
        return arr

    # Находим середину
    mid = len(arr) // 2

    # Рекурсивно сортируем левую и правую половины
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Сливаем две отсортированные половины
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    # Сравниваем элементы из левой и правой частей
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Добавляем оставшиеся элементы (если одна из частей закончилась)
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Проверка
print(merge_sort([3, 2, 1]))  # [1, 2, 3]
print(merge_sort([38, 27, 43, 3, 9, 82, 10]))  # [3, 9, 10, 27, 38, 43, 82]
