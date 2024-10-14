# Refactoring
import json


def greet_user():
    """greet the user by name"""
    filename= 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input('what is your name cute? ')
        with open(filename, 'w') as f:
            json.dump(username,f)
            print(f"we will remember you next time {username}")
    else:
        print(f"welcome back {username}")

# refactoring we split the above function to more functions to improve it
def get_stored_username():
    """get stored username if available"""
    file_name = 'username.json'
    try:
        with open(file_name) as f:
            username= json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """prompt for a new username if there is none"""
    user_name = input(f"hello whats your name? ")
    file_name = 'username.json'
    with open(file_name) as f:
        json.dump(user_name,f)
        return user_name

def greet_user():
    """greet the user by name"""
    user_name = get_stored_username()
    if user_name:
        print(f"welcome back {user_name}")
        check = input(f"Is this your user name,(Y/N)?: ")
        if check.lower()== 'y':
            print(f"thank you for logging in {user_name}")
        else:
            user_name = get_new_username()
            print(f"we will remember you when you come back {user_name}")

greet_user()


# page 282
