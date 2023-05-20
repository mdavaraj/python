# Objective - Object class Part 2
# 1. To get used to basic computing object creation and object method calling
# 2. Able to differentiate between static function and object function

# What to do
# ==========
# create a object function get_price() and return a price for the car
# create a static function get_price(model) and return a price for the car

# Honda City - SGD 20k
# Honda Accord - SGD 30k
# Toyota Vios- SGD 20k
from car import Car

# car = Car()

# YOU should able to print the car model and price below

# print ('Your car price is', car.get_price())
# print ('Your car price is', car.get_price(car.model))

print("Available Car models Honda City, Honda Accord and Toyota Vios")
car_1 = Car()

# car_1.get_price("honda")

print ('Your car price is', car_1.get_price("Honda Accord"))

