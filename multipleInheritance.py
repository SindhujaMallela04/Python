#parent class 1
class bird:
    def fly (self):
        return "This bird can fly."
    def jump (self):
        return "This bird can jump"
    
#Parent class 2
class Mammal:    
    def walk(self):
        return "This mammal can walk."

#child class
class Bat(bird, Mammal):
    #pass  #combines both the parent classes into one
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
    
    def dance(self):
        return "This bat can dance."

#Object creation
bat = Bat("Spider")
print(bat.fly())
print(bat.walk())
print(bat.dance())
m1 = Mammal()
m1 = bat
print(m1.get_name())