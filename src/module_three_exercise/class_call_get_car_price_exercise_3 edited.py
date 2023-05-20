# What to do
# ==========
# create a object function get_price() and return a price for the car
# create a static function get_price(model) and return a price for the car

# Honda City - SGD 20k
# Honda Accord - SGD 30k
# Toyota Vios- SGD 20k
from module_three_exercise.car import Car

print("Available Car models Honda City, Honda Accord and Toyota Vios")
car1 = Car();
car1.brand = 'Honda';
car1.model = 'City';
car1.price = 20000;

print ('Your car static function return price value is -->' + Car.getPrice(car1.model) );

print ('Your car by Object function return price with condition is -->' + car1.getObjectPrice());


