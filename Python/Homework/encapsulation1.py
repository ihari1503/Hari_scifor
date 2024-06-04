class Car:
  def __init__(self,brand,model,year):
    self.__brand = brand
    self.model = model
    self.year = year
  def getbrand(self):
    return.self.__brand
    
  def acceleration(self):
    print("The {self.model} is accelerating)
          
  mycar = Car(Tesla,Model V,2023)

  print(mycar.model)
  print(mycar.getbrand())
