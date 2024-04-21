from lessons.lesson_18.models.db import engine
from lessons.lesson_18.models.base import Base


def main():
    print(
        Base.metadata.tables
    )  # если не проинициализировали в __init__, то Metadata будет пустая
    Base.metadata.create_all(
        bind=engine
    )  # к этому моменту должны быть проинициализированы все классы


if __name__ == "__main__":
    main()
