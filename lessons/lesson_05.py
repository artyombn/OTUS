"""
- Генераторы, next(), yield
- Менеджер контекста (для автоматического действия с открытым блоком после завершения работы с ним)
- List comprehension
- filter(func callback, iterable) - применяет функцию к каждому элементу последовательности и возвращает только те элементы, для которых функция возвращает True.
- map(func callback, iterable) - применяет функцию к каждому элементу последовательности и возвращает новую последовательность, содержащую результаты применения функции к каждому элементу.

Повторить:
- filter()
- map()
- zip()
"""

from math import sqrt
from contextlib import contextmanager

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    for num in (n * n for n in numbers):  # генератор
        print("square is", num)

    squares_g = (n * n for n in numbers)
    print(squares_g)  # <generator object main.<locals>.<genexpr> at 0x100f91120>
    print(next(squares_g)) # 1
    print(next(squares_g)) # 4
    print(next(squares_g)) # 9
    for s in squares_g:  # генерирует след. обращение
        print(f's: {s}')
        if s > 100:
            break

    print(next(squares_g))

# yield - если присутствует в теле ф-ции, то Python автоматически делает из нее генератор
def rnd_numbers_generator():
    # rolled a dice
    print("Test") # не будет отображено
    yield 6 # yield делает передачу значения и ставит на паузу выполнение ф-ции
   # на этом этапе генератор встает на паузу

    print("Another test")
    yield 5

def call():
    print(rnd_numbers_generator())
    print(next(rnd_numbers_generator()))
    print('pause')
    print(next(rnd_numbers_generator()))
    print('another pause')
    print(next(rnd_numbers_generator()))



"""
Пример с числами Фибоначчи, когда хотим сделать какое-то повторяющее действие, при этом
мы не можем спрогнозировать какое кол-во итераций мы хотим сделать
--- Каждое следующее число равно сумме предыдущих ---
"""

def fib(n):
    """
    fib (0) = 0
    fib (1) = 1
    fib(n) = fib(n-1) + fib(n-2)
    """

    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b

    return a

def fib_generator():
    a = 0
    b = 1
    while True:
        yield a # чтобы изначально получить без подсчета
        a, b = b, a + b

def fibonachi():
    print([fib(i) for i in range(11)])
    f = fib_generator()
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))





if __name__ == '__main__':
    main()
    call()
    fibonachi()


# Менеджер контекста
"""
with open('example.txt', 'r') as file:
    data = file.read()
    работа с содержимым файла

После завершения блока кода файл будет автоматически закрыт,
независимо от того, было ли исключение или нет
"""
# Также можно получить через декоратор
@contextmanager
def func_01():
    pass


# List comprehension
items = ['Apple', '', 'Peech', 'Orange', 'Raspberry']
# result = [item for item in items if item]
result = [item
          for item in items
          if item]
print(*result)

# filter(func callback, iterable)
def check(n):
    return f'2 x {n}' # не введет желаемое, так как filter() возвращает либо True, либо False и в данном случае поскольку тут не пусто, то вернет просто значения
# для исправления ситуации лучше использовать генератор (пример ниже)

items_f = filter(check, items)  # применяй колбек (в данном случае ф-ция check) к каждому элементу списка

print('using generator')
items_f_gen1 = (check(item) for item in items if item) # через генератор применяем ф-цию
print(list(items_f_gen1))

print('using map')
items_f_gen2 = map(check, items)
print(list(items_f_gen2))

# map(func callback, iterable)

def square2(n):
    return n * n

def square_test():
    numbers = [1, 2, 3, 4, 5, 54, 32, 11, 7, 8, 2, 1, 67, 98, 92]
    squares = [square2(i) for i in numbers] # using list comprehension
    print(squares)

    squares2 = map(square2, numbers) # using map()
    print(list(squares2))

print(square_test())

numbers3 = [1, 2, 3, 4, 5, 54, 32, 11, 7, 8, 2, 1, 67, 98, 92]
x = map(lambda x: x ** 2, numbers3)
print(list(x))