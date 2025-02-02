from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def profession(self):
        pass
    def introduce(self):
        self.profession()
    
class Engineer(Father):
    def profession(self):
        print("Hey this is my Engineer Son.")

class Doctor(Father):
    def profession(self):
        print("Hey this is my Doctor daughter.")

engineer = Engineer()
engineer.introduce()

doctor = Doctor()
doctor.introduce()

