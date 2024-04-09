"""
Встроенные модули Python

os - модуль взаимодействия с системой
os.name
os.path.dirname(__file__)
print(__file__)
os.listdir(<path>) - посмотреть все файлы (будут добавлены в список)
os.path.sep
os.path.join("Item1", "item2", "item3")  # Item1/item2/item3
os.path.exists(<path>)
os.path.isdir(<path>) # является ли директорией
os.path.isfile(<path>)
os.getcwd() # тоже самое, что и pwd в терминале

ls ~  -> домашняя директория
os.path.expanduser("~") - заменяет символ тильды (~) в пути к файлу на домашнюю директорию текущего пользователя.

with open(<filepath>, "w")  # открыть файл контекстным менеджером.
    f.write("text")

"w" - режим открытия файла, если нет - создаст файл
"a" - Добавляет инфо в конец сущ. файла или создает файл если он не существует
"ab" - для добавления данных в конец файла в бинарном режиме (a - режим добавления, то есть в конец без перезаписи, b - бинарный режим)
"r" - режим чтения файла (можно без "r", просто with open(<filepath>))
f.read()
f.seek(0) - начать чтение файла с начала. 0 - с нулевого элемента

os.remove(filepath)
os.unlink(filepath) # тоже само что remove


посмотреть:
partial
functools.partial - это функция, которая используется для создания новой функции на основе существующей,
фиксируя значения некоторых аргументов.
Удобно, когда нужно использовать функцию с некоторыми аргументами, но оставить другие аргументы для изменения во время вызова новой функции.
"""

import os
from pprint import pprint

print(os.name) #posix

IS_WINDOWS = os.name == 'nt'  # False, should be posix

BASE_DIR = os.path.dirname(__file__)  # shows only directory

print("OS_name:", os.name)
print("IS_WINDOWS:", IS_WINDOWS)
# print("BASE_DIR:", BASE_DIR)
#
# print(__file__)  # /Users/artembn/Python/OTUS/lessons/lesson_11/main.py


def demo_dirs():
    print("BASE_DIR:", BASE_DIR)
    print("local files:", os.listdir(BASE_DIR)) # ['file.txt', 'demo_pathlib', 'demo_pathlib.py', 'main.py']
    print("os.path.sep:", os.path.sep)  # посмотреть разделитель адресных строк
    print(os.path.join("Desktop", "images", "cat"))  # Desktop/images/cat
    print(os.path.exists("Desktop/images/cat"))  # False
    print(os.path.exists("/Users/artembn/Python"))  # True
    print("BASE_DIR exists?", os.path.exists(BASE_DIR))  # BASE_DIR exists? True
    print("is BASE_DIR dir?", os.path.isdir(BASE_DIR)) # True
    print("is BASE_DIR file?", os.path.isfile(BASE_DIR))  # False
    current_file = __file__
    print("current_file:", current_file)
    print("is current_file file?:", os.path.isfile(current_file)) # True
    print(os.getcwd())
    home_dir = os.path.expanduser("~") # если мы хотим делать что-то относительно пользовательской директории
    print(home_dir)  # /Users/artembn
    # Пример для папки с кешом
    my_app_cashe_dir = os.path.join(home_dir, ".cashe/my-app")
    print(my_app_cashe_dir)


def demo_files():
    filename = "file.txt"
    filepath = os.path.join(BASE_DIR, filename)
    print("filepath:", filepath)  # /Users/artembn/Python/OTUS/lessons/lesson_11/file.txt
    print("filepath exists?:", os.path.exists(filepath)) # False
    print("is filepath file?", os.path.isfile(filepath)) # False

    # file = open(filepath, "w")
    # file.write("Hello World") # Лучше не делать, поскольку если ошибка, файл не закроется
    # file.close()
    # Используем контекстный менеджер
    with open(filepath, "w") as f:
        f.write("Hello World\n")
        f.write("hello again\n")

    if os.path.isfile(filepath):
        print("delete file")
        # os.remove(filepath)
        os.unlink(filepath)


    with open(filepath, "w") as f:
        res = f.write("First line\n")
        print("Wrote bytes:", res)

    with open(filepath, "a") as f: # Добавляет инфо в конец сущ. файла или создает файл если он не существует
        f.write("Test append\n")
        f.write("append again\n")
        f.writelines([
            "John\n",
            "Sam\n",
            "Doe\n",
            "Jay\n",
            "Non\n",
            "Kurt\n",
        ])

    with open(filepath, "ab") as f:
        f.write(b"Hi there!\n")
        f.write(bytes([10, 97]))  # 10 -> это байт "\n", 97 -> "a"

    print()
    print("____________________________________")
    print("READING FILE:")
    print("____________________________________")
    with open(filepath) as f:  # Плохой подход, так как приходится хранить весь файл в памяти.
        file_data = f.read()
        print(file_data)
        print("____________________________________")
        print(f"Repr form: {repr(file_data)}")

    print("____________________________________")
    print("END READING")
    print("____________________________________")

    # НУЖНО читать файл по строчкам
    print()
    print()
    with open(filepath) as f:
        for line in f:
            print(repr(line))
            if "Sam" in line:
                print("met Sam. stop reading")
                break  # файл ещё не закрыт. можно продолжить

        print(repr(next(f)))
        print(repr(next(f)))
        print("continue cycle")
        for line in f:
            print(repr(line))

        f.seek(0) # начать чтение файла с начала
        print(repr(next(f)))
        print(repr(next(f)))
        print(repr(next(f)))
        print()
        print()








def main():
    demo_dirs()
    demo_files()
    # print(dict(os.environ))
    pprint(dict(os.environ))


if __name__ == '__main__':
    main()