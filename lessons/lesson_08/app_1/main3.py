from pprint import pprint
from users import create, update, delete as delete_user

pprint(locals())

def main():
    create("John")
    create("Sam")

    update("John", age=20, city="New York")
    update("Sam", email="sam@example.com", job="Software Engineering")

    delete_user("Nick")

if __name__ == "__main__":
    main()