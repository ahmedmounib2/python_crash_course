# Importing a Module into a Module

"""a set of classes that represent electric batteries"""

from car_class import Car  # imported Car class in this electric_car_class module We also need to update
                           # the Car module so it contains only the Car class:

class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """print a statement about the range the battery provides"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 310
        print(f"This car can go {range} miles on a full charge")

    def upgrade_car(self):
        """check the battery size and upgrade it if its not 100 kwh"""
        if self.battery_size < 100:
            self.battery_size = 100
            print(f"the battery was upgraded to {self.battery_size} kwh new battery")
        else:
            print(f"The battery is already upgraded")



class Electric_car(Car):
    """modeling an electric car"""
    def __init__(self,make, model, year):
        super(Electric_car, self).__init__(make,model,year)
        self.battery = Battery()

