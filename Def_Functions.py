

# using a function with a while loop:

def tell_me_name(first_name,last_name):
    """return a full name neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name")
    f_name = input("firstname: ")
    l_name = input("Last name: ")

    name= tell_me_name(f_name,l_name)
    print(f"\nHello, {name}!")
