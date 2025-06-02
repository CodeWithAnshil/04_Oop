class Car:
   def __init__(self,brand,model):
       self.brand=brand
       self.model=model
   def full_name(self):
       return f"{self.brand} {self.model}"
              
class ElectricCar(Car):
     def __init__(self,brand,model,battery_size):
         super().__init__(brand,model)
         self.battery_size=battery_size

tesla_car=ElectricCar("Tesla","model S","88kwh")  
my_car=Car("Toyota","Corolla")
my_new_car=Car("Rang Rover","Defendar")

print(tesla_car.full_name())
print(tesla_car.brand)
print(tesla_car.model)
print(tesla_car.battery_size)

