class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0 
# Object creation
car1 = Car("Toyota", "Corolla")
print(car1.brand)   # Toyota
print(car1.model)   # Corolla

class Student:
    def __init__(self, name, age):
        self.name = name      # Attribute
        self.age = age

    def greet(self):          # Method
        return f"Hello, my name is {self.name}."
