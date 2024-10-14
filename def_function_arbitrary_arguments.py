# Passing an Arbitrary Number of Arguments
#  The asterisk in the parameter name *toppings tells Python to make an
# empty tuple called toppings and pack whatever values it receives into this
# tuple. The print() call in the function body produces output showing that
# Python can handle a function call with one value and a call with three values.
# It treats the different calls similarly. Note that Python packs the arguments
# into a tuple, even if the function receives only one value:

def make_pizza(*toppings):
    """print the list of toppings that have been requested"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushroom','peporoni','hot dog')

def make_cake(*fillings):
    """summarize the cake we are about to make"""
    print("\nMaking a cake with the following fillings:")
    for filling in fillings:
        print(f"-{filling}")

make_cake('chocolate')
make_cake('strawberry','chocolate','caramel')


def make_sandwich(size, *toppings):
    """summarize the sandwich we are about to make"""
    print(f"\nMaking a {size}-inch sandwich with the following fillings:")
    for topping in toppings:
        print(f"-{topping}")

make_sandwich(22,'pepperoni')
make_sandwich(30,'chicken','beef','mushroom','cheese')


# Using Arbitrary Keyword Arguments
# write functions that accept as many key-value
# pairs as the calling statement provides

def build_profile(first,last, **user_info):
    """Build a dictionary containing everything we know about a user"""
    user_info['first_name']= first
    user_info['last_name']= last
    return user_info

user_profile = build_profile('albert','einstien', location='princeton',field='physics')
print(user_profile)

# <The definition of build_profile() expects a first and last name, and then it
# allows the user to pass in as many name-value pairs as they want. The double
# asterisks before the parameter **user_info cause Python to create an empty
# dictionary called user_info and pack whatever name-value pairs it receives into
# this dictionary. Within the function, you can access the key-value pairs in
# user_info just as you would for any dictionary.
