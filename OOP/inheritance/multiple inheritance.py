class Car:
     def __init__(self, c_name, brand, fueltype):
        self.c_name = c_name
        self.brand = brand
        self.fueltype = fueltype

class Bike:
    def __init__(self, b_name, engine_capacity):
        self.b_name = b_name
        self.engine_capacity = engine_capacity

class Vehical(Car, Bike):
    def __init__(self, c_name, brand, fueltype, b_name, engine_capacity, model_no):
         Car.__init__(self, c_name, brand, fueltype)
         Bike.__init__(self, b_name, engine_capacity)
         self.model_no = model_no
    def display(self):
         print(f"Car Name: {self.c_name}, Brand: {self.brand}, Fuel Type: {self.fueltype}")
         print(f"Bike Name: {self.b_name}, Engine Capacity: {self.engine_capacity}cc")
         print(f"Model Number: {self.model_no}")
veh = Vehical("Tesla Model S", "Tesla", "Electric", "Yamaha R15", 155, "V12345")
veh.display()