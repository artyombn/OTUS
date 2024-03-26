#users actions
def create(name):
    print(f'Created user {name=}')
    return ...

def update(name, **kwargs):
    print(f'Updated user {name} with {kwargs=}')

def delete(name):
    print(f'Deleted user {name=}')


print(__file__)
print(__name__)

def main():
    create("John")
    create("Sam")

    update("John", age=20, city="New York")
    update("Sam", email="sam@example.com", job="Software Engineering")

    delete("Sam")

if __name__ == "__main__":  # если модуль запускается через импорт, то его название будет не __main__ а users
    main()

print("END of users module")



