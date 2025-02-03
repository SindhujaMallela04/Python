from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self):
        self.__brand_name = "Yamaha"
    @abstractmethod
    def max_speed(self):
        pass

class Car(Vehicle):
    def max_speed(self):
        return "200 km/h"

class Bike(Vehicle):
    def max_speed(self):
        return "150 km/h"
    
car_obj = Car()
print(f"This is {car_obj._Vehicle__brand_name} Car.")
print(f"The max speed of the car is {car_obj.max_speed()}")

bike_obj = Bike()
print(f"The brand of the bike is {bike_obj._Vehicle__brand_name}.")
print(f"The maximum speed of the bike is {bike_obj.max_speed()}.")

