# classes
class Dog:
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")


my_dog.sit()
my_dog.roll_over()

your_dog = Dog('lucy', 3)
print(f"\nyour dog's name is {your_dog.name}")
print(f"\nyour dog's age is {your_dog.age}")


class Restaurant:
    """a simple restaurant model"""
    def __init__(self,restaurant_name, cuisine_type):
        """initialize name and attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        """print information about restauran name and cuisine"""
        print(f"Restaurant name is {self.restaurant_name}, and its cuisine is {self.cuisine_type} ")
    def open_restaurant(self):
        """print a message that the restaurant is open"""
        print(f"{self.restaurant_name} is now Open.")

restaurant_1 = Restaurant('spectra', 'oriental')

print(f"{restaurant_1.restaurant_name} has just opened in our neighborhood.")
print(f"the restaurant {restaurant_1.restaurant_name} is specialised in the {restaurant_1.cuisine_type} cuisine")
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

restaurant_2 = Restaurant('KFC', 'fast food')
restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()

restaurant_3 = Restaurant('la manzana','spanish cuisine')
restaurant_3.describe_restaurant()
restaurant_3.open_restaurant()


class User:
    """model a User"""
    def __init__(self,first_name,last_name,age, nationality):
        """initialize name and attributes"""
        self.first_name = first_name
        self.last_name= last_name
        self.age= age
        self.nationality = nationality
    def descibe_user(self):
        """print a summary about the user"""
        print(f"\nUser {self.first_name} {self.last_name} is {self.age} year's old, and the nationality is, "
              f"{self.nationality}")

    def greet_user(self):
        """print a greeting about the user"""
        print("\nhello", self.first_name,'',self.last_name, "welcome on board")

ahmed = User('ahmed','medhat',35, 'egyptian')
khaled= User('khaled','medhat',35,'egyptian')
maria= User('maria','sandra',19, 'french')

ahmed.descibe_user()
ahmed.greet_user()

khaled.descibe_user()
khaled.greet_user()

maria.descibe_user()
maria.greet_user()

# excercises 9-4/9-5
class Restaurant:
    """a simple restaurant model"""
    def __init__(self,restaurant_name, cuisine_type):
        """initialize name and attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.numbers_served = 0
    def describe_restaurant(self):
        """print information about restauran name and cuisine"""
        print(f"Restaurant name is {self.restaurant_name}, and its cuisine is {self.cuisine_type} ")
    def open_restaurant(self):
        """print a message that the restaurant is open"""
        print(f"{self.restaurant_name} is now Open.")
    def set_served_customers(self, served):
        """set the numbers of customers served"""
        self.numbers_served = served
    def increment_served_customers(self,increment):
        """add to the numbers of served customers"""
        self.numbers_served += increment


restaurant_1 = Restaurant('spectra', 'oriental')

print(restaurant_1.numbers_served)

restaurant_1.numbers_served = 25
print(restaurant_1.numbers_served)

restaurant_1.set_served_customers(120)
print(restaurant_1.numbers_served)

restaurant_1.increment_served_customers(1000)
print(restaurant_1.numbers_served)


class User:
    """model a User"""
    def __init__(self,first_name,last_name,age, nationality):
        """initialize name and attributes"""
        self.first_name = first_name
        self.last_name= last_name
        self.age= age
        self.nationality = nationality
        self.login_attempt = 0
    def descibe_user(self):
        """print a summary about the user"""
        print(f"\nUser {self.first_name} {self.last_name} is {self.age} year's old, and the nationality is, "
              f"{self.nationality}")

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

ahmed = User('ahmed','medhat',35, 'egyptian')

ahmed.increment_login_attempt()
ahmed.show_login_attemp()

ahmed.reset_login_attempt()
ahmed.show_login_attemp()

ahmed.increment_login_attempt()
ahmed.increment_login_attempt()
ahmed.increment_login_attempt()
ahmed.increment_login_attempt()
ahmed.increment_login_attempt()
ahmed.increment_login_attempt()
ahmed.increment_login_attempt()
ahmed.increment_login_attempt()
ahmed.increment_login_attempt()
ahmed.increment_login_attempt()
ahmed.increment_login_attempt()
ahmed.show_login_attemp()

ahmed.reset_login_attempt()
ahmed.show_login_attemp()
