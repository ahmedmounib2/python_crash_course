prompt = '\nplease enter your preffered pizza topings:'
prompt += '\nenter Quit when you are done '
chosen_pizza = []
while True:
    pizza_topping = input(prompt)
    pizza = chosen_pizza.append(pizza_topping)
    if pizza_topping.lower() == 'quit':
        break
    print(f"You added: {chosen_pizza}, need to add any more toppings?")
###########################################################################################
prompt = '\nplease enter your age, to get the ticket price'
prompt += "\n enter 'Quit' to quit"
prompt+= '\nEnter your age here: '
active = True
while active:
    age = input(prompt)
    if age.lower() == 'quit':
        active = False
        break
    age = int(age)
    if age <= 3:
        print('ticket is free')
    elif age >= 12:
        print('ticket is 20$')
    elif age < 12:
        print('your ticket is 10$')

###########################################################################################

prompt = '\nplease enter 5 preffered sandwich fillings:'
prompt += '\n enter quit if you are done with less than 5 fillings: '
chosen_pizza = []
filling_count = 0
while True:
    pizza_topping = input(prompt)
    filling_count += 1
    if filling_count == 5:
        print(f'you chose 5 out of 5 fillings: {chosen_pizza}')
        break
    elif pizza_topping.lower() == 'quit':
        print(f'you added: {chosen_pizza}')
        break
    pizza = chosen_pizza.append(pizza_topping)
    print(f"You added: {chosen_pizza}, need to add any more toppings?")
