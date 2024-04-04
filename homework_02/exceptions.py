"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class BaseException(Exception):
    def __init__(self, message="Base Exception"):
        super().__init__(message)

class LowFuelError(BaseException):
    def __init__(self):
        print("Low Fuel")

class NotEnoughFuel(BaseException):
    def __init__(self):
        print('Not Enough Fuel')

class CargoOverload(BaseException):
    def __init__(self):
        print('Cargo Overloaded')