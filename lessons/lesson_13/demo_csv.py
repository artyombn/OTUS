import os
import csv

CARS_DIR = os.path.dirname(__file__)
CARS_CSV = os.path.join(CARS_DIR, "cars.csv")
print("CARS_CS path:", CARS_CSV)

USERS_DIR = CARS_DIR
USER_CSV_FILE = os.path.join(USERS_DIR, "users.csv")
print("USER_CSV_FILE path:", USER_CSV_FILE)


def demo_read_csv_cars():
    with open(CARS_CSV, "r") as f:
        reader = csv.reader(f)
        print(reader)
        for i in reader:
            print(i)


def demo_read_csv_cars_dict():
    with open(CARS_CSV, "r") as f:
        reader = csv.DictReader(
            f, delimiter=","
        )  # delimiter="," указываем какой разделитель

        # for car in reader:
        #     print(car)

        for car in reader:  # type: dict
            print(
                "<<",
                car["Make"],
                car["Model"],
                ">>",
                "year:",
                car["Year"],
                "price:",
                car["Price"],
            )


class FieldName:
    username = "username"
    email = "email"
    phone = "phone"


def demo_write_csv():
    fieldnames = [  # используется для списка названия столбцов
        FieldName.username,
        FieldName.email,
        FieldName.phone,
    ]
    with open(USER_CSV_FILE, "w") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()  # запись только заголовков таблицы

        writer.writerow(  # запись строки в таблицу
            {
                FieldName.username: "John",
                FieldName.email: "john@example.com",
                FieldName.phone: "555-555-5555",
            }
        )
        data = [
            {
                FieldName.username: "Tom",
                FieldName.email: "Tom@example.com",
                FieldName.phone: "444-444-444",
            },
            {
                FieldName.username: "Sam",
                FieldName.email: None,
                FieldName.phone: "666-666-666",
            },
        ]
        writer.writerows(data)


def main():
    demo_read_csv_cars()
    print()
    print()
    demo_read_csv_cars_dict()
    print()
    print()
    demo_write_csv()


if __name__ == "__main__":
    main()
