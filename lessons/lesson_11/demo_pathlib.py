"""
pathlib - модуль, который предоставляет объектно-ориентированный интерфейс для работы с путями к файлам и директориями
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
print(repr(Path(__file__).resolve()))
print("BASE_DIR:", BASE_DIR)  # /Users/artembn/Python/OTUS/lessons/lesson_11

def demo_paths():
    # venv_path = Path(".venv").resolve()
    venv_path = BASE_DIR / "demo_pathlib" # / - разделитель пути
    print(venv_path)
    print("is file?", venv_path.is_file()) # False
    print("is dir?", venv_path.is_dir()) # False

    print(Path.home())  # посмотреть домашнюю директорию
    print(Path.cwd()) # текущая рабочая директория
    home_path = Path.home()
    cache_dir = home_path / "cache" / "myapp.json"
    print(cache_dir)  # /Users/artembn/cache/myapp.json

    # for path in BASE_DIR.glob("**/*.py"):
    for path in BASE_DIR.iterdir():
        print(path, f"(is dir?: {path.is_dir()}), (is file?: {path.is_file()})")

def demo_paths_two():
    # cats_dir = Path.cwd()
    cats_dir = BASE_DIR / "pics" / "cats"
    print(cats_dir, "is dir?", cats_dir.is_dir()) # нет такой директории
    # Создаем директорию и файл в ней
    cats_dir.mkdir(parents=True, exist_ok=True)
    cats_dir_readme = cats_dir / "README.md"
    cats_dir_readme.write_text("Cats pics directory\n")

    print()
    print(cats_dir_readme.read_text())
    with cats_dir_readme.open("r") as f:
        for line in f:
            print(repr(line))




if __name__ == '__main__':
    demo_paths()
    demo_paths_two()