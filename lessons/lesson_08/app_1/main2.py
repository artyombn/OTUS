"""
- Модули и Импорты
*если модуль запускается через импорт, то его название будет не __main__ а как название модуля

"""
import users as us_mod
import products as pr_mod
import items_processor as ip

def users():
    return ["users"]

def main():
    print(users())

    us_mod.create ("John")
    us_mod.create ("Sam")

    us_mod.update("John", age=20, city="New York")
    us_mod.update("Sam", email="sam@example.com", job="Software Engineering")

    pr_mod.create ("Laptop")
    pr_mod.create ("Tablet")

    print(ip)
    print(ip.ItemsProcessor)


if __name__ == "__main__":
    main()