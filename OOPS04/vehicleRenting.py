from abc import ABC, abstractmethod

"""Same as Java Vehicle Renting app"""
"""Goal is for the learners to understand abstract methods & interfaces in python"""

class Rentable(ABC):
    @abstractmethod
    def rent(self):
        pass

    @abstractmethod
    def return_item(self):
        pass


class Car(Rentable):
    def __init__(self, car_model):
        self.car_model = car_model
        self.is_rented = False

    def rent(self):
        if not self.is_rented:
            self.is_rented = True
            print(f"Car {self.car_model} is now rented")
        else:
            print(f"Car {self.car_model} is already rented")

    def return_item(self):
        if self.is_rented:
            self.is_rented = False
            print(f"Car {self.car_model} is now returned")
        else:
            print(f"Car {self.car_model} is not rented")


class Bicycle(Rentable):
    def __init__(self, bicycle_model):
        self.bicycle_model = bicycle_model
        self.is_rented = False

    def rent(self):
        if not self.is_rented:
            self.is_rented = True
            print(f"Cycle {self.bicycle_model} is now rented")
        else:
            print(f"Cycle {self.bicycle_model} is already rented")

    def return_item(self):
        if self.is_rented:
            self.is_rented = False
            print(f"Cycle {self.bicycle_model} is now returned")
        else:
            print(f"Cycle {self.bicycle_model} is not rented")
