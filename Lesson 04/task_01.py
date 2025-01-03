class Vehicle():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class ElectricVehicle():
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity
    
    def charge(self):
        return self.battery_capacity

    def get_range(self):
        return self.battery_capacity * 5

class GasolineVehicle():
    def __init__(self, fuel_capacity):
        self.fuel_capacity = fuel_capacity
    
    def refuel(self):
        return self.fuel_capacity

    def get_range(self):
        return self.fuel_capacity * 20

class HybridCar(Vehicle, ElectricVehicle, GasolineVehicle):
    def __init__(self, make, model, year, battery_capacity, fuel_capacity):
        ElectricVehicle.__init__(self, battery_capacity)
        GasolineVehicle.__init__(self, fuel_capacity)
        Vehicle.__init__(self, make, model, year)

car = HybridCar("Toyota", "Prius", 2020, 5, 20)

print(f"The battery capacity for {car.make} {car.model} is {car.charge()} and the range is {car.get_range()}")

# Print the method resolution order
print(HybridCar.__mro__)