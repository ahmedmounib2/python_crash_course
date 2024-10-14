sandwich_orders = ['tuna sandwich','turkey wrap','cheese canape','chicken club sandwich']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"i made you {sandwich} sandwich" )
    finished_sandwiches.append(sandwich)

print("\ni made you these sandwiches")
for sandwich in finished_sandwiches:
    print(sandwich)
sandwich_orders = ['tuna sandwich','pastrami','turkey wrap','pastrami','pastrami','cheese canape','chicken club sandwich']
finished_sandwiches = []


while sandwich_orders:
    while 'pastrami' in sandwich_orders:
        print("the deli has run out of pastrami")
        sandwich_orders.remove('pastrami')
        print("Available sandwiches:", sandwich_orders)
    sandwich = sandwich_orders.pop()
    print(f"I made you {sandwich.title()} sandwich" )
    finished_sandwiches.append(sandwich)

print("\nI made you these sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich.title())


poll_result = {}

poll_active = True
while poll_active:
    name = input('\nWhat is you name?: ')
    response = input('\n what city would you like to visit?: ')
    poll_result[name] = response
    repeat = input('\nwould you like to let anyone else participate?: Yes/No')
    if repeat.lower() == 'no':
        poll_active = False

print('\n___Poll Results___')
for name, response in poll_result.items():
    print(f"{name.title()} would like to visit {response.title()}")
