from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    started = False

    def __init__(self, weight=10, fuel=24, fuel_consumption=2):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError
        else:
            print("Started already")

    def move(self, distance):
        self.distance = distance

        if self.fuel >= self.fuel_consumption * self.distance:
            self.fuel -= self.fuel_consumption * self.distance
        else:
            raise NotEnoughFuel


if __name__ == "__main__":
    a = Vehicle(weight=10, fuel=24, fuel_consumption=2)
    print(a.__dict__)
    a.start()
    a.move(10)