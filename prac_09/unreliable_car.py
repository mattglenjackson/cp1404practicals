from car import Car
from random import randint


class UnreliableCar(Car):
    """Represents an Unreliable Car object."""

    def __init__(self, name='', fuel=0, reliability=0.0):
        """Initialize an instance of an Unreliable Car"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance if drive chance is less than reliability."""

        drive_chance = randint(0, 100)
        if drive_chance < self.reliability:
            super().drive(distance)
        else:
            distance = 0
            return distance

