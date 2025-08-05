# вход
# 5
# 4 5 7 9 11 13
# 6 - number

# выход
# 2

#         l   m      r
# массив: 4 5 7 9 11 13

#         l m r
# массив: 4 5 7 9 11 13

#           l r
# массив: 4 5 7 9 11 13

# обработка последних двух элементов
# if array[l] < number:
#     return r
# else:
#     return l

# array[l]

# l   m    r
# 5 7 9 11 13


def binary_search(array: list[int], number: int) -> int:
    """Функция находит позицию указанного числа number в отсортированном
    по возрастанию массиве array.

    Использует паттерн binary search.
    Временная сложность O(log(n)) - асимптотика binary search
    Пространственная сложность O(1) - добавляемые переменные не зависят
    от размера массива.

    Args:
        array (list[int]): отсортированный по возрастанию массив целых чисел.
        number (int): число, которое мы ищем в массиве.

    Returns:
        int: индекс, числа найденного в массиве или индекс, где это число
        должно находиться, чтобы сохранить порядок сортировки.
    """
    left = 0
    right = len(array) - 1

    # бинарный поиск до схождения к двум последним элементам
    while right - left > 1:
        middle = left + (right - left) // 2

        # визуализация работы алгоритма
        print_pointers_on_array(array, left, right, middle)

        if array[middle] == number:
            return middle

        if number < array[middle]:
            right = middle
        else:
            left = middle

    # обработка последних двух элементов
    print_pointers_on_array(array, left, right, middle)

    if array[left] < number:
        return right
    else:
        return left


def print_pointers_on_array(array, left, right, middle):
    pointers_viz = [" " * len(str(num)) for num in array]
    pointers_viz[left] = "l" + adding_spaces(left, pointers_viz)
    pointers_viz[middle] = "m" + adding_spaces(middle, pointers_viz)
    pointers_viz[right] = "r" + adding_spaces(right, pointers_viz)
    print(" ".join(pointers_viz))
    print(" ".join(str(num) for num in array))


def adding_spaces(position, pointers_viz):
    return (len(pointers_viz[position]) - 1) * " "
