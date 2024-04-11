"""
- Запись данных в JSON
- Чтение данных из файла JSON и работа с ними
"""

import json
from datetime import datetime, date, timedelta, timezone
from pprint import pprint


# def custom_json_encoder(obj):
#     if isinstance(obj, datetime):
#         return str(obj)
#
#     return str(obj)


def custom_json_encoder(obj):  # для форматирования даты и времени
    if isinstance(obj, date):
        return (
            obj.isoformat()
        )  # формат времени ISO --> {'created_at': '2024-04-11T16:48:53.222477+03:00'}

        # return obj.strftime("%d.%m.%Y")  # {'created_at': '11.04.2024'}

    message = f"Type {type(obj)} not serializable"
    raise TypeError(message)


def dump_json_demo():
    data = {
        "data": {
            "users": [
                {
                    "id": 1,
                    "name": "Николай",
                    "email": "john@example.com",
                },
                {
                    "id": 2,
                    "name": "Sam",
                    "email": None,
                },
            ],
            "posts": [
                {
                    "id": 1,
                    "title": "P1",
                    "published": True,
                    "created_at": datetime.now(tz=timezone.utc),
                },
                {
                    "id": 2,
                    "title": "P2",
                    "published": False,
                    "created_at": datetime.utcnow() - timedelta(days=1),
                },
                {
                    "id": 3,
                    "title": "P3",
                    "published": True,
                    "created_at": datetime.now(tz=timezone(timedelta(hours=3))),
                },
            ],
        },
        "meta": {
            "page": 1,
            "per_page": 10,
        },
    }
    print(data)

    json_string = json.dumps(  # для записи данных в формате JSON
        data,
        default=custom_json_encoder,
        indent=2,
        ensure_ascii=False,  # указывает, следует ли кодировать все не-ASCII символы в выводе JSON
    )
    print(json_string)

    with open("demo_json.json", "w") as f:  # запись в файл
        json.dump(
            data,
            f,
            default=custom_json_encoder,
            indent=2,
            ensure_ascii=False,
        )


def load_json_demo():  # чтение из файла
    with open("demo_json.json", "r") as f:
        data = json.load(f)

    pprint(data)
    for user in data["data"]["users"]:
        print("User info:", user)


def main():
    dump_json_demo()
    load_json_demo()
    assert json.loads("null") is None


if __name__ == "__main__":
    main()
