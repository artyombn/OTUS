"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class BaseException(Exception):
    def __init__(self, message="Базовое исключение"):
        super().__init__(message)

class LowFuelError(BaseException):
    print(f'Низкий уровень топлива')

class NotEnoughFuel(BaseException):
    print(f'Недостаточный уровень топлива')

class CargoOverload(BaseException):
    print(f'Перегрузка груза')