"""
namedtuple - не используем, поскольку есть некоторые проблемы (наример при сравнении содержимого разных классов в случае, если само содержимое одинаковое)

"""

from collections import namedtuple

Person = namedtuple("Person", "name, age, rating, email")

def get_person_as_tuple():
    name = "John Smith"
    age = 42
    email = None
    return name, age, email

def get_person_as_namedtuple():
    name = "John Smith"
    age = 42
    rating = 7
    email = None
    return Person(name, age, rating, email)


def main():
    person = get_person_as_tuple()
    print(person)
    print("name:", person[0])
    print("age:", person[1])
    print("email:", person[2])

    p2 = get_person_as_namedtuple()
    print(p2)
    print(type(p2).mro())
    print("name:", p2.name)
    print("age:", p2.age)
    print("email:", p2.email)
    print("rating:", p2.rating)

    example()


Point = namedtuple("Point", "x, y")
PersonCharacteristics = namedtuple("PersonCharacteristics", "height, weight")

def example():
    p1 = Point(y=10, x=20)
    print(p1)
    p2 = Point(20, y=10)
    print(p2)
    print("p1 == p2", p1 == p2)
    # p1.x = 123  # AttributeError: can't set attribute нельзя изменить так как tuple()
    p3 = Point(150, 60)
    p_chars = PersonCharacteristics(height=150, weight=60)
    print(p_chars)
    print("p_chars == p3", p_chars == p3) # они будут равны несмотря на то, что это разные классы
    print(type(p3).mro()) # [<class '__main__.Point'>, <class 'tuple'>, <class 'object'>]
    print(type(p_chars).mro()) # [<class '__main__.PersonCharacteristics'>, <class 'tuple'>, <class 'object'>]



if __name__ == "__main__":
    main()