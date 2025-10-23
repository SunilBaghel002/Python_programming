class Characters:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def call(self):
        print(f"{self.name} {self.age}")
name_1 = Characters("sunil", 21)

name_1.call()


class Car():
    def set_details(self, brand, color):
        self.brand = brand
        self.color = color
    def show_details(self):
        print(f"This car is a {self.brand} {self.color}")

car1 = Car()
car1.set_details("BMW M4", "Black")
car2 = Car()
car2.set_details("Tata", "black")

car1.show_details()
car2.show_details()