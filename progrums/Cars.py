'''
Cars.py
This is a Class Progrum to name different car makes, models, and year
'''
#class
class Car:
  def __init__(self, make, model, gas_mileage, year):
#Attributes of car
    self.make = make
    self.model = model
    self.gas_mileage = gas_mileage
    self.year = year
  #Bretts Car 
Brett_car = Car('Nissan', 'Sentra', 12, 2008)

print(Brett_car.make)
print(Brett_car.model)
print(Brett_car.gas_mileage)
print(Brett_car.year)

#Doms Car
Dom_car = Car('Subaru', 'Outback', 15, 2018)

print(Dom_car.make)
print(Dom_car.model)
print(Dom_car.gas_mileage)
print(Dom_car.year)

#Scotts Car
Scott_car = Car('Honda', 'Civic', 10, 2020)

print(Scott_car.make)
print(Scott_car.model)
print(Scott_car.gas_mileage)
print(Scott_car.year)

#Using if statement to see if you have enough gas to make the trip
#bretts gas mileage
if (Brett_car.gas_mileage >= 13):
  print('Brett has enough gas to make it')
else:
  print('Brett does not have enough gas to make it')
  #Scott gas mileage
  if (Scott_car.gas_mileage >= 13):
    print('Scott has enough gas to make it')
  else:
    print('Scott does not have enough gas to make it')
    #Dom gas mileage
    if (Dom_car.gas_mileage >= 12):
      print('Dom has enough has to make it')
    else:
      print('Dom does not have enough gas to  make it')