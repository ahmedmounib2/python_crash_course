def make_pizza(*toppings):
    """print the list of toppings that have been requested"""
    print(toppings)


def make_cake(*fillings):
    """summarize the cake we are about to make"""
    print("\nMaking a cake with the following fillings:")
    for filling in fillings:
        print(f"-{filling}")


def make_sandwich(size, *toppings):
    """summarize the sandwich we are about to make"""
    print(f"\nMaking a {size}-inch sandwich with the following fillings:")
    for topping in toppings:
        print(f"-{topping}")


def build_profile(first,last, **user_info):
    """Build a dictionary containing everything we know about a user"""
    user_info['first_name']= first
    user_info['last_name']= last
    return user_info
