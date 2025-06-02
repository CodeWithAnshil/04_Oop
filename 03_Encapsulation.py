class Car:
   def __init__(self,brand,model):
       self.__brand=brand
       self.__model=model
   def full_name(self):
       return f"{self.__brand} {self.__model}"
              
   def get_brand(self):
       return self.__brand
   def get_model(self):
       return self.__model
   
  
my_car=Car("Toyota","Corolla")
my_new_car=Car("Rang Rover","Defendar")

print(my_car.get_brand())
print(my_car.get_model())
print(my_car.full_name())
# print(my_car.__brand)  it will show AttributeError : 'Car' object has no attribute '__brand'
