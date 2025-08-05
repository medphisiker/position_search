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

        if array[middle] == number:
            return middle

        if number < array[middle]:
            right = middle
        else:
            left = middle

    # обработка последних двух элементов
    if array[left] < number:
        return right
    else:
        return left


if __name__ == "__main__":
    array_len = int(input())
    array = list(map(int, input().split()))
    number = int(input())

    position = binary_search(array, number)
    print(position)
