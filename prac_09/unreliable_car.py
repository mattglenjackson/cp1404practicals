from car import Car
from random import randint


class UnreliableCar(Car):
    """Represents an Unreliable Car object."""

    def __init__(self, name='', fuel=0, reliability=0.0):
        """Initialize an instance of an Unreliable Car"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance if random generated number is less than reliability

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """

        random_number = randint(0, 100)
        if random_number < self.reliability:
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self._odometer += distance
            return distance
        else:
            distance = 0
            return distance
