"""
OOP - Object-Oriented Programming
mro() - получение списка родительских классов при множественном наследовании
__slots__ - установка св-в класса (запрещает установку др. св-в)
просмотр доступных св-в класса: экземпляр.__slots__

vars(экземпляр класса) # то же самое, что экземпляр.__dict__

Основные концепции ООП:
Инкапсуляция
Наследование
Полиморфизм
Абстракция

- Наследование - создание новых классов на основе существующих (наследование св-в, методов родителя)
Тот, кто наследует - подкласс или производный класс
Тот, от кого наследуется - суперкласс или базовый класс
"""

class User:
    """User class"""
    # Свойства класса
    MIN_AGE = 21

    def __init__(self, name, age, email=None):  # Ф-ция класса == magic method
        self.name = name
        self.age = age
        self.email = email

    def increase_age(self):  # Метод экземпляра класса (то есть не сработает без создания экземпляра)
        self.age += 1

user_john = User(name="John", age=42)  # Создание экземпляра класса
user_sam = User(name="Sam", age=55)

print(user_john)
print(user_john.name, user_john.age)  # John 42
print(user_sam.name, user_sam.age)  # Sam 55

print(user_sam.__dict__)  # {'name': 'Sam', 'age': 55}
print(vars(user_sam)) # тоже самое что user_sam.__dict__
print(User.__dict__)

user_john.increase_age()      # вызов через метод на экземпляре класса
print(user_john.name, user_john.age)  # John 43
User.increase_age(user_john)  # вызов через метод на классе
print(user_john.name, user_john.age)  # John 44

user_john.email = "john@mail.ru"
print(user_john.email)

print(User.MIN_AGE)
print(user_john.MIN_AGE) # MIN_AGE берется со свойств класса
# отредактировать глобально можно только через свойства класса

User.MIN_AGE = 90 # сработает замена, редактирование идет через св-ва класса
user_john.MIN_AGE = 80 # сработает только для экземпляра класса john
print(user_john.MIN_AGE)
print(user_sam.MIN_AGE) # берет из свойств класса

print(User.__eq__) # метод сравнения объектов класса
print(User.__eq__ is object.__eq__)  # True
print(User.mro())  # для получения списка родительских классов при множественном наследовании



class User2:
    __slots__ = ("name", "age", "email")  # Класс имеет только такие свойства, другие нельзя добавить

    def __init__(self, name, age, email=None):
        self.name = name
        self.age = age
        self.email = email

    def increase_age(self):
        self.age += 1

user2_john = User2("John2", age=25)
user2_john.email = "john222@example.com"
user2_sam = User2("Sam2", age=31)

print(user2_john.name, user2_john.age, user2_john.email) # John2 25 john222@example.com

# print(user2_sam.__dict__)
# AttributeError: 'User2' object has no attribute '__dict__'

# user2_sam.homepage = "www.homepage.com"
# AttributeError: 'User2' object has no attribute 'homepage'
print(user2_sam.__slots__)  # ('name', 'age', 'email') - единственные св-ва которые есть


# Наследование

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a) # берем параметры из родительского инита, но поскольку b нам не нужно, заменяем на a
        self.a = a

    def area(self):
        return self.a * self.a

# Поскольку выполняют одну ф-цию, и почти похожи,  наследуем Square от Rectangle


# Второй вариант записи
class Square(Rectangle):
    def __init__(self, a):
        self.a = a

    @property
    def b(self): # сделать из этого метода свойство (property) которое сразу читает значение b как значение a из класса родителя
        return self.a

    @b.setter
    def b(self, value):
        self.a = value



class User3:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name

    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f"(first_name={self.first_name!r}, last_name={self.last_name!r}")


user3_john = User3("John", "Doe")
user3_sam = User3("Sam", "White")
print(user3_john)
print(user3_sam)
print([user3_john, user3_sam])

print(user3_sam.first_name)
print(user3_sam.last_name)
print(user3_sam.full_name)
