# Excercise 9-8 9-9

class User:
    """model a User"""
    def __init__(self,first_name,last_name,age, nationality):
        """initialize name and attributes"""
        self.first_name = first_name
        self.last_name= last_name
        self.age= age
        self.nationality = nationality
        self.login_attempt = 0
    def describe_user(self):
        """print a summary about the user"""
        long_name= f"\nUser {self.first_name} {self.last_name} is {self.age} year's old, and the nationality is, {self.nationality}"
        return long_name.title()

    def greet_user(self):
        """print a greeting about the user"""
        print("\nhello", self.first_name,'',self.last_name, "welcome on board")

    def show_login_attemp(self):
        """show hom many login attempts were made"""
        print(f"The user made {self.login_attempt} log in attempts")

    def increment_login_attempt(self):
        """increments the login attempts made by 1"""
        self.login_attempt += 1

    def reset_login_attempt(self):
        """reset the login attempts to 0"""
        self.login_attempt = 0

class Priviliges:
    """define priviliges for users"""
    def __init__(self,privilige):
        self.privilige = privilige
        self.privilige = ['add user','remove user','ban user']
    def add_privilige(self,privilige_add):
        """add privilige to the list of priviliges"""
        if privilige_add is not None:
            self.privilige.append(privilige_add)
    def show_privilige(self):
        """print the user priviliges"""
        print(f"The user have the current priviliges: {self.privilige}")


class Admin(User):
    def __init__(self,first_name,last_name,age,nationality):
        super().__init__(first_name,last_name,age,nationality)
        self.privilige = Priviliges(privilige=self)          # adding the priviliges class to admin class
                                                # by making a Privilages instance as an attribute in the class


ahmed = Admin('ahmed','medhat',35,'egyptian')

print(ahmed.describe_user())

ahmed.show_login_attemp()
ahmed.privilige.show_privilige()
ahmed.privilige.add_privilige('can fly around')
ahmed.privilige.show_privilige()

class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """print a statement showing the cars mileage"""
        print(f" This car has {self.odometer_reading} miles on it")

    def update_odometer(self,mileage):
        """set the odometer reading to the given value, Reject the change if it attempts roll the odometer back"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll the odometer back!")
    def increment_odometer_reading(self,miles):
        """add the given amount to the odometer reading"""
        self.odometer_reading += miles

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

tesla = Electric_car('tesla','model s', 2019)

print(tesla.get_descriptive_name())
tesla.battery.describe_battery()
tesla.battery.get_range()
tesla.battery.upgrade_car()
tesla.battery.get_range()
tesla.battery.upgrade_car()




