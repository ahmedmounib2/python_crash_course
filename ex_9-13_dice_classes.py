# excercis 9-13 

"""6 sided dice classe"""

from random import randint


class Die:
    """modeling a dice with 6 sides"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """rolling the dice and picking a number to print"""
        return randint(1, self.sides)

di = Die()

results = []
for roll_number in range(10):
    result = di.roll_die()
    results.append(result)

print(f"\nbelow is the result after rolling a 6 sided Dice 10 times:")
print(results)



"""10 sided dice class"""

class Die10:
    """modeling a dice with 10 sides"""

    def __init__(self, sides=10):
        self.sides = sides

    def roll_die(self):
        """rolling the dice and picking a number to print"""
        return randint(1, self.sides)

di10 = Die10()

results = []
for roll_number in range(10):
    result = di10.roll_die()
    results.append(result)

print(f"\nbelow is the result after rolling a 10 sided Dice 10 times:")
print(results)


"""so sided dice class"""

class Die20:
    """modeling a dice with 20 sides"""

    def __init__(self, sides=20):
        self.sides = sides

    def roll_die(self):
        """rolling the dice and picking a number to print"""
        return randint(1, self.sides)

di20 = Die20()

results = []
for roll_number in range(10):
    result = di20.roll_die()
    results.append(result)

print(f"\nbelow is the result after rolling a 20 sided Dice 10 times:")
print(results)
