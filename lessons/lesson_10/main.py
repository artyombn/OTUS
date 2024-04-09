"""
- Тесты

Запуск теста
python -m unittest
Запуск теста с подробностями
# python -m unittest -v <path to the module>

self.assertEqual(expected, result)
with self.subTest(msg, item1, item2, ...,  expected) - Позволяет проверить остальные тесты в случае падения одного из тестов (в цикле)

PYTEST
python -m pytest
pytest <file/directory> -s -vv

Запустить только провалившиеся тесты
pytest <file/directory> -v --last-failed

Декоратор для нескольких параметров
    @pytest.mark.parametrize(
        "a, b, expected",
        [(1, 2, 3), (4, 5, 9), (3, 4, 7)]
    )

ФИКСТУРЫ
@pytest.fixture()

"""

