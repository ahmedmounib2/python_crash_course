# ex 10-11

import json
filname = 'faer.json'

def get_fav_number():
    """prompt users for their favorite numbers and store it in a file"""
    fav_num = input('whats your favorite number? ')
    with open(filname,'w') as f:
        json.dump(fav_num, f)
        print(f"thanks we will remember that your favorite number is: {fav_num}")


# ex 10-12

def read_fav_num():
    """show the favorite number"""
    try:
        with open(filname) as f:
            num = json.load(f)
            print(f"I know you favorite number!, it is: {num}")
    except FileNotFoundError:
        prompt = 'we couldnt find this file'
        prompt += ' whats your fav num. and we will store it in a file? '
        num = input(prompt)
        with open(filname, 'w') as f:
            json.dump(num, f)
            print(f"thanks , now we stored your favorite number: {num}")

get_fav_number()

read_fav_num()

# ex 10-13
filename = 'username.json'

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
    with open(file_name, 'w') as f:
        json.dump(user_name,f)
        return user_name

def greet_user():
    """greet the user by name"""
    user_name = get_stored_username()
    if user_name:
        print(f"welcome back {user_name}")
        check = input(f"Is this your user name,(Y/N)?: ")
        if check.lower() == 'y':
            print(f"welcome back {user_name}")
        elif check.lower() == 'n':
            user = get_new_username()
            print(f"we will remember you when you come back {user}")


greet_user()
