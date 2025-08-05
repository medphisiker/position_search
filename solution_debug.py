# вход
# 5
# 4 5 7 9 11 13
# 6 - number

# выход
# 2

#         l     m    r
# массив: 4 5 7 9 11 13

#         l m r
# массив: 4 5 7 9 11 13

#           m
#           l r
# массив: 4 5 7 9 11 13

#           m
#           r
#             l
# массив: 4 5 7 9 11 13


def find_insert_position(array: list[int], target: int) -> int:
    """Функция находит позицию указанного числа target в отсортированном
    по возрастанию массиве array.

    Использует паттерн binary search.
    Временная сложность O(log(n)) - асимптотика binary search
    Пространственная сложность O(1) - добавляемые переменные не зависят
    от размера массива.

    Args:
        array (list[int]): отсортированный по возрастанию массив целых чисел.
        target (int): число, которое мы ищем в массиве.

    Returns:
        int: индекс, числа найденного в массиве или индекс, где это число
        должно находиться, чтобы сохранить порядок сортировки.
    """
    # обработка пустого массива
    if not array:
        return 0

    # оптимизация для значений лежащих вне диапазона массива
    if target <= array[0]:
        return 0
    if target > array[-1]:
        return len(array)

    left, right = 0, len(array) - 1

    # стандартный бинарный поиск с визуализацией
    while left <= right:
        mid = left + (right - left) // 2

        # визуализация работы алгоритма
        print_pointers_on_array(array, left, right, mid)

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # если элемент не найден, left указывает на позицию для вставки
    return left


def print_pointers_on_array(array, left, right, middle):
    # Проверка границ массива перед доступом к элементам
    pointers_viz = [" " * len(str(num)) for num in array]

    # Добавляем указатели, проверяя границы
    if 0 <= middle < len(array):
        pointers_viz[middle] = "m" + adding_spaces(middle, pointers_viz)
    if 0 <= left < len(array):
        pointers_viz[left] = "l" + adding_spaces(left, pointers_viz)
    if 0 <= right < len(array):
        pointers_viz[right] = "r" + adding_spaces(right, pointers_viz)

    print(" ".join(pointers_viz))
    print(" ".join(str(num) for num in array))


def adding_spaces(position, pointers_viz):
    return (len(pointers_viz[position]) - 1) * " "
