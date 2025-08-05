from solution_debug import find_insert_position


def run_single_test(array, number, expected_position, test_name=""):
    print(f"\n--- Running test: {test_name} ---")
    print(f"array: {array}")
    print(f"number: {number}")
    print(f"expected_position: {expected_position}")
    position = find_insert_position(array, number)
    print(f"actual_position: {position}")
    assert position == expected_position, f"Test failed for {test_name}: expected {expected_position}, got {position}"
    print(f"--- Test {test_name} passed ---")


def test():
    # Тесты на вставку в начало
    run_single_test([5, 7, 9, 11, 13], 4, 0, "Insert before first element")
    run_single_test([5, 7, 9, 11, 13], 5, 0, "Insert at first element")
    
    # Тесты на вставку в середину
    run_single_test([5, 7, 9, 11, 13], 6, 1, "Insert between 5 and 7")
    run_single_test([5, 7, 9, 11, 13], 8, 2, "Insert between 7 and 9")
    run_single_test([5, 7, 9, 11, 13], 10, 3, "Insert between 9 and 11")
    run_single_test([5, 7, 9, 11, 13], 12, 4, "Insert between 11 and 13")
    
    # Тесты на вставку в конец
    run_single_test([5, 7, 9, 11, 13], 13, 4, "Insert at last element")
    run_single_test([5, 7, 9, 11, 13], 15, 5, "Insert after last element")
    
    # Тесты на поиск существующих элементов
    run_single_test([5, 7, 9, 11, 13], 5, 0, "Find first element")
    run_single_test([5, 7, 9, 11, 13], 7, 1, "Find second element")
    run_single_test([5, 7, 9, 11, 13], 9, 2, "Find middle element")
    run_single_test([5, 7, 9, 11, 13], 11, 3, "Find fourth element")
    run_single_test([5, 7, 9, 11, 13], 13, 4, "Find last element")
    
    # Тесты для четного количества элементов
    run_single_test([5, 7, 9, 11, 13, 16], 6, 1, "Insert in even array between 5 and 7")
    run_single_test([5, 7, 9, 11, 13, 16], 14, 5, "Insert in even array between 13 and 16")
    run_single_test([5, 7, 9, 11, 13, 16], 16, 5, "Find last element in even array")
    
    # Тесты для маленьких массивов
    run_single_test([5, 7], 6, 1, "Insert in 2-element array")
    run_single_test([5, 7], 4, 0, "Insert before 2-element array")
    run_single_test([5, 7], 8, 2, "Insert after 2-element array")
    
    # Тесты для одноэлементного массива
    run_single_test([5], 5, 0, "Find in 1-element array")
    run_single_test([5], 3, 0, "Insert before 1-element array")
    run_single_test([5], 7, 1, "Insert after 1-element array")
    
    # Тест для пустого массива
    run_single_test([], 5, 0, "Insert in empty array")


if __name__ == "__main__":
    test()