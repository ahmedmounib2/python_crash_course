# using or adding parameters to functions

def greet_user(name):
    print(f"hi there ,{name}!")
    print('welcome on board')


print("start")
greet_user("john")
greet_user("mary")
print("finish")

# these are position arguments

def greet_user(first_name, last_name):
    print(f"hi there ,{first_name} {last_name}!")
    print('welcome on board')


def square(number):
    return number*number

print(square(3))

print("start")
greet_user("john", "smith")
print("finish")

# using keyword arguments if we dont care about the position of the argument and we need to improve readability of the code

def greet_user(first_name, last_name):
    print(f"hi there ,{first_name} {last_name}!")
    print('welcome on board')


print("start")
greet_user( last_name="smith", first_name="john")
print("finish")


# we can add a keyword argument with positiona argument , but always write positional arguments 1st

def greet_user(first_name, last_name):
    print(f"hi there ,{first_name} {last_name}!")
    print('welcome on board')


print("start")
greet_user( "john", last_name="smith")
print("finish")
