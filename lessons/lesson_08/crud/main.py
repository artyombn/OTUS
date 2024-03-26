"""
Основной main лекции лежит в /Users/artembn/Python/OTUS/lessons/lesson_08/app_1/main.py
"""
#
# from users.create import create
# # from users.update import update
# from users import update

from lessons.lesson_08.crud import users


# from users import *

def main():
    print('Hello main!')

    users.create("John")
    users.create("Sam")

    users.update_user("John", age=20, city="New York")
    users.update_user("Sam", email="sam@example.com", job="Software Engineering")

    # products.create ("Laptop")
    # products.create ("Tablet")


if __name__ == "__main__":
    main()