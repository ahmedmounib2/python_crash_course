# Importing a Module into a Module
# made a module called car_class and stored only the car class in it
# made module called electric_car_class and imported car_class to it in a file

from electric_car_class import Electric_car as ec

tesla = ec('tesla', 'model x', 2023)

print(tesla.get_descriptive_name())

from car_class import  Car

hyundai = Car('hyundai','matrix', 2005)

print(hyundai.get_descriptive_name())

