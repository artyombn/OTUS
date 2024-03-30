"""
Использование:
dataclass - быстренько сделать какой-нибудь класс + не хотим ставить сторонние пакеты
pydantic - валидация, приведение типов, конвертация, дополнительные фишки со словарями (превращение)

https://pypi.org - поиск пакетов Pythin
pip install pydantic

Посмотреть:
attrs - альтернатива dataclass, имеет больше возможностей
(отдельный python пакет)
"""
from dataclasses import dataclass, field
# from typing import Optional

x: int = 123  # аннотация типа

@dataclass(slots=True)  # slots - запрещает добавлять другие атрибуты классу
class Person:  # добавляем в класс аннотацию типа. Python её не будет валидировать
    name: str
    age: int
    # email: Optional[str] = None
    email: str | None = None

    def increase_age(self):
        self.age += 1


class MyPerson:  # для нормального отображения пришлось писать много магических методов
    # поэтому декоратор @dataclass лучше, поскольку эти методы автоматически включены в нем
    def __init__(self, name: str, age: int, email: str | None = None):
        self.name = name
        self.age = age
        self.email = email

    def __str__(self):
        return (f"{self.__class__.__name__}"
                f"(name={self.name!r}, "
                f"age={self.age!r}, "
                f"email={self.email!r})")

    def __repr__(self):
        return str(self)

@dataclass(frozen=True)
class Food:
    name: str
    weight: int
    # tags: list[str] = [] # будет ошибка поскольку frozen делает все атрибуты неизменяемыми
    tags: list[str] = field(default_factory=list)
def get_person() -> Person:
    p = Person("John Smith", age=42)
    return p

def main():
    p = get_person()
    p2 = Person("Sam Black", age=33, email="sam@example.com")
    print(p2)
    print(p)
    print(type(p).mro()) # [<class '__main__.Person'>, <class 'object'>]
    p3 = MyPerson("Kate White", 42, "kate@example.com") # <__main__.MyPerson object at 0x104502610>
    p4 = MyPerson("Kyle Gray", 22, "kyle@example.com")
    print(p3)
    print([p3, p4])

    milk = Food(name="Milk", weight=1000)
    print(milk)
    # milk.weight = 900 # поскольку стоит frozen у декоратора над Food, нельзя изменить данные
    # print(milk)
    # p2.lots = 5 # при попытке добавить новый атрибут класса будет ошибка
    # print(p2.lots)
    print(p2.__slots__) # если декоратор не имеет slots=True, тогда будет ошибка. нужно через __dict__
    print(p)
    p.increase_age()
    print(p)


if __name__ == "__main__":
    main()
