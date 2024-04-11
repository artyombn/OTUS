"""
Конфигурация проекта - ini файлы
"""

from configparser import ConfigParser
from pathlib import Path

DEMO_CONFIG_FILE = "demo_config.ini"

port = 1

# with open(DEMO_CONFIG_FILE, "r") as f:
#     config = f.read()
#     print(config)


def demo_configparser():
    global port
    config = ConfigParser()
    config.read(DEMO_CONFIG_FILE)
    print(config)
    print(config.sections())  # ['mysql', 'postgresql', 'files']
    print()
    print(config.items("DEFAULT"))
    print(
        config.items("mysql")
    )  # также будет выведены DEFAULT, потому что он всегда существует
    print()
    print(config["DEFAULT"].get("secret_key"), config["mysql"].get("host"))

    for key, value in config["DEFAULT"].items():
        print(key, value)

    db_conn_info = (
        config.get("mysql", "host"),
        config.get("mysql", "port"),
        config.getint("mysql", "port"),  # выводит port в integer
    )

    print(db_conn_info)
    pg_port = config["postgresql"].getint("port")  # извлечение определенных данных
    print(pg_port)
    port = pg_port + 1
    print(port)

    print(config["DEFAULT"].get("debug"))

    if config["DEFAULT"].getboolean("debug") == True:
        print("DEBUG MODE activated")
    else:
        print("DEBUG MODE deactivated")

    print(config["mysql"].get("user"), config["mysql"].get("password"))

    return config


def config_write():
    global port
    config = ConfigParser()
    config.read(DEMO_CONFIG_FILE)  # сначала чтение файла, затем запись в файл

    config["postgresql"]["port"] = str(port)  # отредактировали значения
    config["files"]["home"] = str(Path.home())
    config["DEFAULT"]["debug"] = str("off")
    config["DEFAULT"]["TestAdd"] = str("NewParam")  # добавление нового параметра

    with open(DEMO_CONFIG_FILE, "w") as f:  # перезаписали значения
        config.write(f, space_around_delimiters=False)  # убрать пробелы в исходном ф-ле


def main():
    demo_configparser()
    config_write()


if __name__ == "__main__":
    main()
