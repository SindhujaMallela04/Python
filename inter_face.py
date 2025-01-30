from abc import ABC, abstractmethod

#interface in python
class NaturalDisaster(ABC):
    @abstractmethod
    def cause(self):
        pass
    def effect(self):
        pass

class Tsunami(NaturalDisaster):
    def cause(self):
        print("The cause of Tsunami is Earthquake under the sea bed.")
    def effect(self):
        print("Effect of Tsunami : City Drowned")
    def warning(self):
        print("Warning : Tsunami Alert")

class Earthquake(NaturalDisaster):
    def cause(self):
        print("The cause of Earthquake is Movement of Tectonic plates")
    def effect(self):
        print("Effect of Earthquake : Huge cracks in the ground")
    def warning(self):
        print("Warning : Earthquake Alert")

def main():
    tsunami = Tsunami()
    earthquake = Earthquake()
    tsunami.cause()
    tsunami.effect()
    tsunami.warning()
    earthquake.cause()
    earthquake.effect()
    earthquake.warning()
main()

    