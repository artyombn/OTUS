"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [i ** 2 for i in args]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def check(x):
    count = 0
    if x < 0:
        return False
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            count += 1
    if count <= 0 and x != 0 and x != 1:
        return True
    else:
        return False


def filter_numbers(input_list, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

    if filter_type == ODD:
        return list(filter(lambda x: x % 2 != 0, input_list))
    elif filter_type == EVEN:
        return list(filter(lambda x: x % 2 == 0, input_list))
    elif filter_type == PRIME:
        return list(filter(check, input_list))
    else:
        print('No filter type')
        return None