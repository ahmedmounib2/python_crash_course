import pizza

pizza.make_pizza(16,'pepperoni')
print(pizza.make_pizza(10,'hotdog'))


# Importing Specific Functions
# You can also import a specific function from a module. Here’s the general
# syntax for this approach:
# from module_name import function_name



# You can import as many functions as you want from a module by
# separating each function’s name with a comma:
from functions_import import make_sandwich, build_profile

make_sandwich(20,'hotdog')

user = build_profile('ahmed','monib', age= 35)
print(user)

from functions_import import make_pizza as mp

mp('shrimp')

import pizza as p

p.make_pizza(26, 'pineapple')

# Importing All Functions in a Module
# You can tell Python to import every function in a module by using the
# asterisk (*) operator:
# from pizza import *

from functions_import import *

make_sandwich(10, 'tuna')
