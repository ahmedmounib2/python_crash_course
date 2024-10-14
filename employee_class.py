# ex 11-3

class Employee:
    """modeling an employee"""
    def __init__(self,first_name,last_name,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, anual_raise= 5000):
        self.anual_raise = anual_raise
        self.salary += self.anual_raise
        return self.salary

    def show_employee(self):
        """show information about the employee"""
        print(f"employee name is {self.first_name} {self.last_name}, his salary is {self.salary}")


