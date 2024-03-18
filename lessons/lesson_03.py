"""
- Функции
- Рекурсия (вложенная функция)
- Любое количество аргументов функции
- В аргументах функции никогда нельзя указывать изменяемые типы
def func(item, tags=[]) - нельзя! при новом вызове функции значение tags будет сохранено от предыдущего вызова
def func(item, tags=None) - в самой функции обрабатываем tags:
    if tags is None:
    tags = []
"""

# ФУНКЦИИ
fruits = ['apple', 'banana', 'cherry']
vegetables = ['potato', 'cucumber']

def print_items(elements):
    if elements:
        None
    else:
        print('no elements')
    for item in elements:
        print(f'- {item}')

print_items(fruits)
print_items(vegetables)


words = ['apple',
         'eggs',
         'banana',
         'house',
         'bicycle',
         'spam',
         'eggs']

numbers = [3, 2, 3, 2, 5, 6]

def contains_duplicates(elements):
    known_elements = set()
    for i in elements:
        if i in elements:
            known_elements.add(i)
        else:
            continue
    return known_elements

print(contains_duplicates(words))
print(contains_duplicates(numbers))


# f(n) = n * f(n-1) - факториал

def factorial(n):
    result = 1
    if n > 0:
        for i in range(1, n+1):
            result *= i
    else:
        result = None
    return result if result is not None else 'Неверное значение'

print(factorial(0))

# Решение через рекурсию (вложенная функция)
"""
Рекурсия имеет лимиты, поэтому например факториал 1000 не может быть вычислен через рекурсию
Стек держит каждое состояние вызова
"""

def factorial_recursion(n):
    if n < 3:  # для избежания ошибки переполнения стека из-за бесконечной рекурсии
        return n
    return n * factorial_recursion(n-1)

print(factorial_recursion(10))

# Любое количество аргументов функции

def hello(name, age, dish):
    print(
        f'Hello {name}!',
        'You are',
        age,
        'and your favourite dish is',
        dish
    )

hello('John', 22, 'pizza')
hello('Vlad', 18, 'french fries')

"""
Функция всегда возвращает 1 элемент
"""
def user_info(user):
    return user, 22, "artemb@gmail.com"

print(user_info("Artem"))  # ('Artem', 22, 'artemb@gmail.com') - tuple
name, age, email = user_info("Артем")
print(name, age, email)

def sum_numbers(*numbers):
    print(numbers)

sum_numbers()  # ()
sum_numbers(1) # (1,)
sum_numbers(2, 3)           # (2, 3)
sum_numbers(5, 6, 'abc', True, 8)  # (5, 6, 'abc', True, 8)


def sum_numbers(*numbers):
    return sum(numbers)

print(sum_numbers(5, 6, 8))

Nick_data = ['Nick', 29, 'Fish']
hello(*Nick_data)