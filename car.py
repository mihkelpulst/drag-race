from random import randint


class Car:
    def __init__(
        self,
        number:int #Car number
        ):
        self.number = number 

    def currentSpeed(self):
        return(randint(1, 3))
