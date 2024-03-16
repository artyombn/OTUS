"""
- Параллельное присваивание
- ??? Метод  get_or_create() - поиск в базе, если не нашел - создает
- Функция для неограниченного кол-ва аргументов *args
*Кортежи атомарные (Python автоматически распаковывает при передаче в функцию
*Списки изменяемые (Python не может автоматически их распаковывать при передаче в функцию)
- Декораторы (Wrapper)
- functools в декораторе - чтобы сохранить докстрингу и название декорируемой ф-ции
- Именованные аргументы функции + **kwargs

Посмотреть:
*args, *kwargs
ф-я get_or_create()
декораторы
"""

import time
import functools

a = 4
b = 'hello'
a, b = b, a  # параллельное присваивание. работает, поскольку в python меняются ссылки

d = b, a # <class 'tuple'>


def render_user_1(username):
    result = f'User {username}'
    return result, username

user_1, tmp = render_user_1('Ivan')
print(user_1)

# метод get_or_create()
# user, created = User_1.get_or_create(username)


def render_user_2(username, address=None):  # address - необязательный аргумент
    result = f'User {username} ({address})'
    if not address:
        result = f'User {username}'
    return result, username


user_2, tmp2 = render_user_2('Ivan')
print(user_2)

# return result, username, address, 5, 10, 18
# user_2, *others = render_user_2('Ivan') - тогда все элементы после username , будут записаны в *args


def sum_sqr(x, y):  # ф-я суммы квадратов
    return x ** 2 + y ** 2

print(sum_sqr(2, 3))

# Если хотим для бесконечного кол-во аргументов

def sum_sqr2(*args):  # неограниченное кол-во аргументов
    return sum(map(lambda x: x ** 2, args))

print(int(sum_sqr2(2, 3, 5, 6)))


data = (1, 2, 3, 4, 'hello')
print(data)  # (1, 2, 3, 4, 'hello')
print(*data) # 1 2 3 4 hello - распаковались

nums = [1, 2, 3, 4, 5, 6]
print(sum_sqr2(*nums))  # просто nums не будет работать, так как нельзя возводить список в квадрат

# Кортежи (tuple) неизменяемы и Python автоматически их распаковывает при передаче в функцию, поскольку кортежи считаются более атомарными
# Списки [list] изменяемы, считаются более контейнерными структурами данных и Python не может распаковывать их автоматически при передаче в функцию. Для этого нужно делать ручную распаковку


# ДЕКОРАТОРЫ (WRAPPER)
# Когда нужно внедрить дополнительное поведение функции

def profile_it(func):
    @functools.wraps(func)  # чтобы сохранить докстрингу и название декорируемой ф-ции
    def inner(*args):  # аргументы декорируемой ф-ции
        start = time.monotonic()

        result = func(*args)

        end = time.monotonic()
        print(f'{end - start} sec')
        return result
    return inner

@profile_it
def render_us(username):
    """ Докстринга для декорируемой ф-ции """
    result = f'User {username}'
    return result
#
user_1 = render_us('Ivan')
print(user_1)
print(render_us.__doc__)
print(render_us.__name__)


def render_user3(username, address="", age=None, **kwargs):
    print(kwargs)
    result = (
        f'User {username} '
        f'({address or "No address"}, {age or "No age"})'
    )

    return result

# Именованные аргументы функции
user_5 = render_user3('Artem', "Moscow", 25)
print(user_5)
# но нам не обязательно соблюдать порядок передачи аргументов, если мы передаем именованные аргументы в функцию
print(render_user3('Artem', age=35, grade="Master", weight=80))