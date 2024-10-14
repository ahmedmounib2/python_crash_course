"""a restaurant class"""

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