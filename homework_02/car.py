"""
создайте класс `Car`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02.engine import Engine

class Car(Vehicle):

    def set_engine(self, engine=0):
        if isinstance(engine, Engine):
            self.engine = engine
        else:
            raise f'Только объект Engine!'