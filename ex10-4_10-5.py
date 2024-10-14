# ex 10-4
# my solution

prompt = 'Hello, please enter your name to log it in the guest book'
prompt += "\nenter 'quit' if you are the last user"
prompt += '\nenter you name here: '

active = True

visitors = []
while active:
        name= input(prompt)
        if name.lower() == 'quit':
            break
        else:
            visitors.append(name)
            print(f"Hi {name.title()}")

ex10_4_file= 'ex10-4file.txt'
with open(ex10_4_file, 'w') as file_object:
    file_object.write(f"These guests visited the website:")
    for visitor in visitors:
        file_object.write(f"\n{visitor.title()}")

# book solution ex 10-4

from pathlib import Path

path = Path('10-4-book-solution.txt')

prompt = '\nHi, whats your name?'
prompt += '\nenter your name: '

guest_names = []
while True:
    name = input(prompt)
    if name.lower() == 'quit':
        break
    print(f"thanks {name.title()} we will add your name in the guest book")
    guest_names.append(name)

file_string = ''
for name in guest_names:
    file_string += f"{name}\n"

path.write_text(file_string.title())


# ex 10-5

from pathlib import Path

answers = []
prompt = "why do you like programming, type quit to end poll: "
while True:
    poll = input(prompt)
    if poll.lower() == 'quit':
        break
    answers.append(poll)


path = Path('exc10-5-file.txt')

file_string = ''
for answer in answers:
    file_string += f"\n{answer}"
    path.write_text(file_string)


