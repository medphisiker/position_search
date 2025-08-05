from solution_debug import binary_search


def test():
    # Тест нечетное число элементов в начале массива
    array = [5, 7, 9, 11, 13]
    number = 6
    correct_position = 1
    
    print(f"\narray:{array}")
    print(f"number:{number}")
    print(f"{correct_position}")
    position = binary_search(array, number)
    print(f"position:{position}")
    assert position == correct_position
    
    # Тест нечетное число элементов в начале массива
    array = [5, 7, 9, 11, 13]
    number = 7
    correct_position = 1
    
    print(f"\narray:{array}")
    print(f"number:{number}")
    print(f"{correct_position}")
    position = binary_search(array, number)
    print(f"position:{position}")
    assert position == correct_position
    
    # Тест нечетное число элементов в начале массива
    array = [5, 7, 9, 11, 13]
    number = 5
    correct_position = 0
    
    print(f"\narray:{array}")
    print(f"number:{number}")
    print(f"{correct_position}")
    position = binary_search(array, number)
    print(f"position:{position}")
    assert position == correct_position
    
    # Тест нечетное число элементов в начале массива
    array = [5, 7, 9, 11, 13]
    number = 4
    correct_position = 0
    
    print(f"\narray:{array}")
    print(f"number:{number}")
    print(f"{correct_position}")
    position = binary_search(array, number)
    print(f"position:{position}")
    assert position == correct_position
    
    # Тест четное число элементов в начале массива
    array = [5, 7, 9, 11, 13, 16]
    number = 6
    correct_position = 1
    
    print(f"\narray:{array}")
    print(f"number:{number}")
    print(f"{correct_position}")
    position = binary_search(array, number)
    print(f"position:{position}")
    assert position == correct_position
    
    # Тест четное число элементов в начале массива
    array = [5, 7, 9, 11, 13, 16]
    number = 7
    correct_position = 1
    
    print(f"\narray:{array}")
    print(f"number:{number}")
    print(f"{correct_position}")
    position = binary_search(array, number)
    print(f"position:{position}")
    assert position == correct_position
    
    # Тест четное число элементов в начале массива
    array = [5, 7, 9, 11, 13, 16]
    number = 5
    correct_position = 0
    
    print(f"\narray:{array}")
    print(f"number:{number}")
    print(f"{correct_position}")
    position = binary_search(array, number)
    print(f"position:{position}")
    assert position == correct_position
    
    # Тест нечетное число элементов в середине массива
    array = [5, 7, 9, 11, 13]
    number = 11
    correct_position = 3
    
    print(f"\narray:{array}")
    print(f"number:{number}")
    print(f"{correct_position}")
    position = binary_search(array, number)
    print(f"position:{position}")
    assert position == correct_position
    
    # Тест нечетное число элементов в середине массива
    array = [5, 7, 9, 11, 13]
    number = 9
    correct_position = 2
    
    print(f"\narray:{array}")
    print(f"number:{number}")
    print(f"{correct_position}")
    position = binary_search(array, number)
    print(f"position:{position}")
    assert position == correct_position
    
    # Тест нечетное число элементов в середине массива
    array = [5, 7, 9, 11, 13]
    number = 10
    correct_position = 3
    
    print(f"\narray:{array}")
    print(f"number:{number}")
    print(f"{correct_position}")
    position = binary_search(array, number)
    print(f"position:{position}")
    assert position == correct_position
    
    # Тест нечетное число элементов в конце массива
    array = [5, 7, 9, 11, 13]
    number = 11
    correct_position = 3
    
    print(f"\narray:{array}")
    print(f"number:{number}")
    print(f"{correct_position}")
    position = binary_search(array, number)
    print(f"position:{position}")
    assert position == correct_position
    
    # Тест нечетное число элементов в конце массива
    array = [5, 7, 9, 11, 13]
    number = 13
    correct_position = 4
    
    print(f"\narray:{array}")
    print(f"number:{number}")
    print(f"{correct_position}")
    position = binary_search(array, number)
    print(f"position:{position}")
    assert position == correct_position
    
    # Тест нечетное число элементов в конце массива
    array = [5, 7, 9, 11, 13]
    number = 12
    correct_position = 4
    
    print(f"\narray:{array}")
    print(f"number:{number}")
    print(f"{correct_position}")
    position = binary_search(array, number)
    print(f"position:{position}")
    assert position == correct_position
    
    # Тест нечетное число элементов в конце массива
    array = [5, 7, 9, 11, 13]
    number = 15
    correct_position = 5  # Исправлено: для числа больше всех элементов позиция должна быть равна длине массива
    
    print(f"\narray:{array}")
    print(f"number:{number}")
    print(f"{correct_position}")
    position = binary_search(array, number)
    print(f"position:{position}")
    assert position == correct_position
    
    # Тест всего 2 элемента в массиве
    array = [5, 7]
    number = 6
    correct_position = 1
    
    print(f"\narray:{array}")
    print(f"number:{number}")
    print(f"{correct_position}")
    position = binary_search(array, number)
    print(f"position:{position}")
    assert position == correct_position
    
    # Тест всего 1 элемент в массиве
    array = [5]
    number = 5
    correct_position = 0
    
    print(f"\narray:{array}")
    print(f"number:{number}")
    print(f"{correct_position}")
    position = binary_search(array, number)
    print(f"position:{position}")
    assert position == correct_position
    
    # Тест пустой массив
    array = []
    number = 5 # любое число
    correct_position = 0  # Для пустого массива позиция всегда 0
    
    print(f"\narray:{array}")
    print(f"number:{number}")
    print(f"{correct_position}")
    position = binary_search(array, number)
    print(f"position:{position}")
    assert position == correct_position

if __name__ == "__main__":
    test()