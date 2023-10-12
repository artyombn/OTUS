from abc import ABC
from homework_02 import exceptions

class Vehicle(ABC):
    weight = None
    started  = None
    fuel = None
    fuel_consumption = None

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = 1
            else:
                raise exceptions.LowFuelError

    def move(self, distance):
        if distance <= (self.fuel / self.fuel_consumption) * 100:
            self.fuel -= (self.fuel_consumption * self.distance) / 100
        else:
            raise exceptions.NotEnoughFuel




