from abc import ABC
from homework_02 import exceptions

class Vehicle(ABC):
    started = False

    def __init__(self, weight=100, fuel=50, fuel_consumption=5, distance=6):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.distance = distance

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError

    def move(self, distance):
        self.distance = distance
        max_distance = self.fuel / self.fuel_consumption
        if self.distance <= max_distance:
            self.fuel = self.fuel - self.fuel_consumption * self.distance
        else:
            raise exceptions.NotEnoughFuel




