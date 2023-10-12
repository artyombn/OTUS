"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02 import exceptions

class Plane(Vehicle):
    cargo = None
    max_cargo = None

    def __init__(self, max_cargo):
        self.max_cargo = max_cargo

    def load_cargo(self, item):
        self.item = item
        if self.item + self.cargo <= self.max_cargo:
            self.cargo += self.item
        else:
            raise exceptions.CargoOverload

    def remove_all_cargo(self):
        previous_cargo = self.cargo
        self.cargo = 0
        return previous_cargo