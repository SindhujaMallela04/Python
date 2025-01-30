#Concrete Method
from abc import ABC, abstractmethod

class NaturalDisaster(ABC):
    @abstractmethod
    def cause(self):
        pass
    def effect(self):
        pass

class Tsunami(NaturalDisaster):
    def cause(self):
        print("Tsunami is caused by Earthquake under seabed")
    def effect(self):
        print("Effect of Tsunami : City Drowned")

class Earthquake(NaturalDisaster):
    def cause(Self):
        print("Earthquake is caused by Movement of Tectonic plates")
    def effect(self):
        print("Effect of Earthquake : Huge cracks in the ground")

def main():
    tsunami = Tsunami()
    earthquake = Earthquake()
    tsunami.cause()
    tsunami.effect()
    earthquake.cause()
    earthquake.effect()
main()


