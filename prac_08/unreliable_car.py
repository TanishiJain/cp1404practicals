import random

from car import Car


class Unreliable_car(Car):

    def __init__(self, name, fuel,reliability):
        super().__init__(name,fuel)
        self.reliability = reliability

    def drive(self,distance):
        random_number = random.randint(0,100)
        if random_number >= self.reliability:
            distance = 0
        drove = super().drive(distance)
        return drove





    def __str__(self):

        return "{}, reliability= {} ".format(super().__str__(), self.reliability)