"""
- Продвинутый ООП
- Инкапсуляция - скрытие реализации (если в св-вах класса в начале названия переменной есть нижнее подчеркивание, разработчик скрывает эту переменную, чтобы
ей не пользовались. Если он добавляет декоратор property для скрытой переменной, то он позволяет ей пользоваться)
Инкапсулированные св-ва и методы НЕЛЬЗЯ вызывать снаружи
- Staticmethod - декоратор (метод, позволяющий использовать обычные ф-ции внутри класса. не ф-ции/методы класса)
Решает проблему наследования, а также импортирования неклассовых ф-ций
- Classmethod - декоратор, который используется для определения метода класса, который принимает первым аргументом ссылку на класс
Этот декоратор позволяет создавать методы, которые могут работать с атрибутами класса, независимо от конкретного экземпляра класса
- Атрибуты класса, доступы к атрибутам класса (для доступа к этому параметру нужен classmethod)
- Установка min и max значений атрибутов класса (валидация)
- Область видимости (LEGB)
- dir(Class) - показать магические методы класса
- Магические методы
Эмуляция функции __call__
Эмуляция контейнерных типов  __len__, __getitem__, __setitem__, __delitem__, __iter__, __contains__  etc
Эмуляция числовых типов  __abs__, __add__, __mul__, __sub__, __truediv__ etc

- Исключения

Повторить:
- setter $ getter
- @staticmethod
- @classmethod
"""

class User:
    MIN_AGE = 18 # атрибут класса

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self._age = age  # инкапсулировали переменную (скрыли реализацию) = protected

    def _clear_age(self, value):  #нельзя вызывать этот метод напрямую
        return int(value)

    def __str__(self):
        return f'{self.__class__.__name__}: {self.full_name}'
# Используя @staticmethod
#
#     @staticmethod
#     def clear_age(value):  # нет обращения к параметру self, поскольку это обычная ф-ция
#     return int(value)
#

    @staticmethod   # обычная ф-ция, делающая данные КАПСОМ
    def create_caps(first_name, last_name, age):
        return User(first_name.upper(), last_name.upper(), age)

    @classmethod
    def create_caps_classmethod(cls, first_name, last_name, age):
        if age < cls.MIN_AGE:
            raise ValueError('Age is too small')
        return cls(first_name.upper(), last_name.upper(), age)


    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name} ({self.age})"

    @property
    def age(self):  # getter (всегда должен что-то вернуть)
        return self._age

    @age.setter
    def age(self, value):  # setter (должен что-то принять)
        self._age = value

    def inc_age(self):
        self._age +=1  # инкапсулировали переменную (скрыли реализацию)

    def __str__(self):
        return self.full_name


user_john = User("John", "Doe", 25)
# user_john.age = '28'
user_john.inc_age() # код сломается, поскольку мы передали строку. НЕ КОНТРОЛИРУЕТСЯ ТИП ДАННЫХ
print(user_john)

# Пользовательское соглашение:
# user_john._age = '30'    ТАК НЕЛЬЗЯ!
# print(user_john._age)    ТАК НЕЛЬЗЯ!
# _age - инкапсулированная переменная, должна оставаться скрытой от глаз

# Чтобы можно было пользоваться age, устанавливаем property, строка 19-21
print(user_john.age)
user_john.age = 99  # AttributeError: property 'age' of 'User' object has no setter



class CustomUser(User):  # может также наследовать статические методы
    pass


user_1 = User("John", "Doe", 25)
user_2 = CustomUser("Ivan", "Ivanov", 28)
print(user_1)
print(user_2)

if isinstance(user_2, CustomUser): # ,будет напечатан поскольку user_2 является экземпляром класса
    print('access granted')

user_3 = User.create_caps('Team', 'Cook', 55)
print(user_3)
user_4 = CustomUser.create_caps('Nikolai', 'Safonov', 79)
print(user_4)

print(isinstance(user_4, CustomUser)) # False, поскольку user_4 наследуется от User
# т.к. ф-ция create_caps яв-я методом класса-родителя

user_5 = CustomUser.create_caps_classmethod('Tifan', 'Urban', 22) # если age < 18 будет ValueError
print(user_5)
print(isinstance(user_5, CustomUser)) # True поскольку создавался с помощью @classmethod


# Область видимости (LEGB) - порядок нахождения значения в области видимости от L к B

# L - local, область, определенная внутри текущей функции
# E - enclosing (замыкающая), область, включающая локальную область, но находящаяся в объемлющей функции
# например: область видимости, относящаяся к области других функций, когда функция вложена в другую.
# G - global, определенная на верхнем уровне модуля
# B - built-in (встроенная)

a = 5  # находится в глобальной области

def my_func():
    #a = 15 - если отсутствует в ф-ции, в локальной области, ищет сначала в замыкающей, а потом в глобальной области
    print(a)

my_func()


class User8:
    MIN_AGE = 18  # class attr  User.MIN_AGE*

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        self.MIN_AGE = 90
        print(f"cls.MIN_AGE = {self.MIN_AGE}")  # 90 -> берет из локальной области, то есть из инициализатора
        print(f"cls.MIN_AGE = {User.MIN_AGE}")  # 18 -> берет из глобальной области, из класса


    def __str__(self):
        return f'{self.first}, {self.last} ({self.age})'

    @classmethod
    def create_new(cls, first, last, age):
        return User8(first, last, age) if age >= cls.MIN_AGE else None


    def __add__(self, other):
        return self.__class__(
            self.first + other.first,
            self.last + other.last,
            self.age + other.age
        )



user8 = User8('Artem', 'Balabashin', 29)
user9 = User8.create_new('Danil', 'Ivanov', 44)

print(dir(User8))
print(user8)
print(user9)
user33 = user8 + user9
print(user33)


class Users:
    def __init__(self):
        self._items = []

    def __str__(self):
        return '  '.join(str(item) for item in self._items)

    def add(self, *items):
        self._items.extend(items)

    def __contains__(self, item):
        return item in self._items   # 0(n)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

otus_users = Users()
otus_users.add(user8)
otus_users.add(user9)
otus_users.add(user8)

print(f"Otus users: {otus_users}")

print(user8 in otus_users)  # argument of type 'Users' is not iterable
# добавляем маг. метод  __contains__  --> строка 179 и тогда работает

print(len(otus_users))

for i, user in enumerate(otus_users):
    print(f'({i}) --> {user}')



# ИСКЛЮЧЕНИЯ

def read_data():
    numbers = []

    try:
        while True:
            user_num = input('Input the number and press Enter (the second Enter will stop input): ')
            if not user_num:
                break
            numbers.append(float(user_num))
    except ValueError as e:
        print(f'The error occurred: {e}')
    else:
        print(f'The len of inputted numbers: {len(numbers)}')
    finally:   # выполняется ВСЕГДА! (обычно используется, чтобы почистить что-то в коде после его выполнения)
        return numbers

# read_data()


"""
try:
    <operation where exception may be occurred>
except ValueError:
    return <do this if exception has been occurred>
    
    
THE 2nd EXAMPLE: 

def div_safe(a,b):
    print(f'Starting from {[a,b]}')

    try:
        c = a/b
    except Exception as z:
        return f'Ты где-то накосячил, ошибка: {z}'
    # return c

    else:
        return c
        
        
        
SEVERAL EXCEPTIONS:

class ClientError(Exception):
    pass
    
class ServerError(Exception):
    pass
    
class WrongAge(ClientError):
    pass

try:
    <operation>
except ClientError as c:
    print('be careful', type(c), c)
except ServerError as s:
    print('check server', type(s), s)
except Exception as e:
    print('strange error occurred', type(e), e)

"""
