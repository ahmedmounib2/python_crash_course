"""admin and priviliges class"""
from user_class import User

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

