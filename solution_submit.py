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
    if target > array[-1] + 1:
        return len(array)
    
    left, right = 0, len(array) - 1
    
    # стандартный бинарный поиск
    while left <= right:
        mid = left + (right - left) // 2
        
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    # если элемент не найден, left указывает на позицию для вставки
    return left


if __name__ == "__main__":
    array_len = int(input())
    array = list(map(int, input().split()))
    number = int(input())

    position = find_insert_position(array, number)
    print(position)
