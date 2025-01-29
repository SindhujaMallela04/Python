#Overriding Example
# class Example:
#     def __init__(self, name):
#         print(f"First Constructor: HEllo {name}")

#     def __init__(self, age):
#         print(f"Second constructor: Age is {age}")

# obj = Example(25)
 #Calls only the second constructor

# class Example1:
#     def __init__(self, *args):
#         if len(args) == 1:
#             print(f"Hello {args[0]}")
#         elif len(args) == 2:
#             print(f"Hello {args[0]}, you are {args[1]} years old.")

# obj1 = Example1(["Sindhuja", 20])

class Example:
    def __init__(self, name, **kwargs):
        self.name = name
        for nam, age in kwargs.items():
            print(f"Hey! {nam}, your age is {age}.")
            

obj = Example("Zoro", Zoro=20)

# class DestructorExample:
#     def __init__(self, name):
#         self.name = name
#         print(f"Object {self.name} is created.")

#     def __del__(self):
#         print(f"Object {self.name} is destroyed.")

#Creare and delere an object
# obj = DestructorExample("sample")
# del obj