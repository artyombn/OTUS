"""
- Модули и Импорты
*если модуль запускается через импорт, то его название будет не __main__ а как название модуля

/ проверить импортирование модулей с классами, работу с этими классами и с ф-циями внутри классов
"""
print("Real start of main module")

import users  # будет выполнен весь код в модуле users
import products

print("Start of main module after imports")

def main():
    print('Hello main!')

    users.create ("John")
    users.create ("Sam")

    users.update("John", age=20, city="New York")
    users.update("Sam", email="sam@example.com", job="Software Engineering")

    products.create ("Laptop")
    products.create ("Tablet")


if __name__ == "__main__":
    main()
    print(__file__)
