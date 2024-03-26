from crud import users
from crud import products


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