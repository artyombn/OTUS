"""
https://pypi.org - поиск пакетов Pythin
pip install pydantic

python -m venv  - посмотреть используемый venv
python -m pip install virtualenv - установка venv

rm -rf <path_to_virtualenv> - удаление venv
python -m venv <path_to_virtualenv> - создание venv

source ./venv/bin/activate - активировать venv
deactivate - деактивация

Посмотреть pydantic Annotated
"""
# from typing_extensions import Annotated
from pydantic import BaseModel, PositiveInt, ConfigDict, Field
from datetime import datetime, date

class Food(BaseModel):
    name: str = Field(min_length=3, max_length=10)
    weight: PositiveInt
    best_before: date = Field(default_factory=date.today)
    tags: list[str] = ["sale"]

class Person(BaseModel):
    model_config = ConfigDict(  # позволяет настроить конфигурацию модели
        # strict=True  # строгие типы атрибутов (обязательно использовать те типы, которые указаны в аннотации)
        strict=False,
        # frozen=True  # сделать неизменяемым
        str_max_length=20 # не более 20 символов для всех полей
        )
    name: str
    age: PositiveInt # PositiveInt - запрещает в атрибутах использовать отрицательные значения
    email: str | None = None
    favorite_food: Food | None = None

    def increase_age(self):
        self.age += 1

def main():
    p = Person(name='Sam Black',
               age="42", # pydantic автоматически конвертирует в нужный тип
               email='sam@example.com')

    print(p)
    print([p])
    print(repr(p))

    p.name = "Sam Grey"
    p.increase_age()
    print(repr(p))

    salad = Food(name='Salad', weight=200)
    print(salad)
    pie = Food(name='Pie', weight=500, tags=["sugar"])
    print(pie)
    cookies = Food(name='Cookies', weight=300)
    cookies.tags.append("sugar") # позволяет клонировать изменяемый объект
    print(cookies)

if __name__ == '__main__':
    main()

