#quiz 5-8 python crash course

usernames = ['ahmed', 'admin','ola']

for username in usernames:
    if username == 'admin':
        print('hello admin, would you like to see a status report')
    else:
        print(f'hello, {username}, thank you for loging in again')
if usernames == []:
    print('we need to find some users')
    ##################################################################################################################


#quiz 5-10 python crash course

current_users = ['ahmed','eman','ola','khaled', 'farida']
for user in range(0, len(current_users)):
    current_users[user] = current_users[user].upper()



new_users = ['eman','ola','khaled', 'habiba','samira']
existing_users = []

name_added = input('please enter your username> ')

while name_added:
    for user in range(0, len(current_users)):
        x = current_users[user] = current_users[user].upper()
        y = current_users[user] = current_users[user].lower()
        z = current_users[user] = current_users[user].title()
        current_users.append(x)
        current_users.append(y)
        current_users.append(z)

    if name_added in current_users:
        print(f'user name already taken, please enter a new name ')
        name_added = input('please enter your username> ')

    else:
        new_users.append(name_added)
        current_users.append(name_added)
        print(f'{name_added} updated successfully')
        break




