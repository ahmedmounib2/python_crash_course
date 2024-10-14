# Excercise 9-6/9-7

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


class Icecream_stand(Restaurant):
    """modeling an icecream stand"""
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['strawberry','vanilla','chococolate']  #adding attribute flavors with a set value
   
    def available_flavors(self):                #method to describe the available flavors
        """show available flavors"""
        print(f"the current available flavors are {self.flavors}")
       
    def add_new_flavor(self,flavor):         #method to append the flavor to our list of flavors , in attribte flavors
        """add a new flavor to the list of flavors"""
        if flavor is not None:
            self.flavors.append(flavor)
        else:
            self.flavors = ['strawberry','vanilla','chococolate']

   
       
       
iceice = Icecream_stand('fluffy ice', 'desserts')   # instance running
iceice.describe_restaurant()
iceice.available_flavors()

iceice.add_new_flavor('caramel')
iceice.available_flavors()

iceice.add_new_flavor('pistachio')
iceice.available_flavors()




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
       
       
class Admin(User):
    def __init__(self,first_name,last_name,age,nationality):
        super().__init__(first_name,last_name,age,nationality)
        self.priviliges = ['can add post', 'can delete post', 'can ban user']
   
    def show_priviliges(self):
        """print the admin priviliges"""
        print(f"the Admin {self.first_name} {self.last_name} have the following priviliges:")
        print(f"{self.priviliges}")
       
    def add_priviliges(self,privilige):
        """add more priviliges to admin"""
        if privilige is not None:
            self.priviliges.append(privilige)
        else:
            self.priviliges = ['can add post', 'can delete post', 'can ban user']

       
       
       
admin_one = Admin('ahmed','medhat', 35 ,'egyptian')

print(admin_one.describe_user())

admin_one.show_priviliges()

admin_one.add_priviliges('can dance and jump around')
admin_one.show_priviliges()

