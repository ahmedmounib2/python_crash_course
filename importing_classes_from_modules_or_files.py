# importing classes
# adding Car class, Electric_car and Battery class in a separate file to import them
#file name: my_car

from my_car import Car, Electric_car

my_new_car = Car('audi','a4',2023)

print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading= 1500
my_new_car.read_odometer()

my_electric_car = Electric_car('tesla','model s',2019)
print(my_electric_car.get_descriptive_name())

my_tesla = Electric_car('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# we can also import the entire car module by : import my_car but to access each
#Here’s what it looks like to import the entire car module and then create a
# regular car and an electric car:
import my_car

my_beetle = my_car.Car('volkswagen','beetle',2009)
print(my_beetle.get_descriptive_name())

mercedes_e = my_car.Electric_car('Mercedes', 'Eqx', 2012)
print(mercedes_e.get_descriptive_name())

