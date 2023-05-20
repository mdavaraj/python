# Objective - Object class Part 1
# 1. To get used to basic computing object creation and object method calling
# 2. Able to differentiate between static function and object function

# What to do
# ==========
# Use call_person.py as reference, initialize the car object as Honda City 
# then print the value belowmy

# car = Car()

# YOU should able to print the car brand and model below
# print('brand--->' , car.brand )
# print('model--->'  , car.model )
# print('price--->'  , car.price )

from car import Car


mycar = Car()
mycar.brand = " Honda"
mycar.model = "city"
mycar.price = "$15000"


mycar2 = Car()
mycar2.brand = "Toyota"
mycar2.model = "Supra"
mycar2.price = "$30000"

mycar3 = Car()

print('brand--->' , mycar.brand )
print('model--->'  , mycar.model )
print('price--->'  , mycar.price )
print("")
print('brand--->' , mycar2.brand )
print('model--->'  , mycar2.model )
print('price--->'  , mycar2.price )


print("What car brand do you like?")
mycar3.brand =input()
print("What model from "+ mycar3.brand + " Do you like?")
mycar3.model = input()
print("How much did you pay for it? ")
mycar3.price = input()
print(f"You like {mycar3.brand} {mycar3.model} and you paid $ {mycar3.price} for it")


