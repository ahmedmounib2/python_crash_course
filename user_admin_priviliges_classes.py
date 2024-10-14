"""classes user, priviliges, and admin"""

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

