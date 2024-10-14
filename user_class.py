"""class user"""

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

