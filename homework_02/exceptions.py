"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class LowFuelError(Exception):
    print(f'Низкий уровень топлива')

class NotEnoughFuel(Exception):
    print(f'Недостаточный уровень топлива')

class CargoOverload(Exception):
    print(f'Перегрузка груза')