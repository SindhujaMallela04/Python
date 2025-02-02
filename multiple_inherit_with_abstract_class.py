from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def get_name(self):
        pass

class Employee(ABC):
    @abstractmethod
    def get_salary(self):
        pass

class Manager(Person, Employee):
    def get_name(self):
        print("Hey i am the manager")
    def get_salary(self):
        print("My salary is 500000 per month")

manager = Manager()
manager.get_name()
manager.get_salary()