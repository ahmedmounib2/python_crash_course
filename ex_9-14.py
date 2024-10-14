# exc. 9-14

from random import choice

possibilities = [1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e']

winning_ticet = []

while len(winning_ticet) < 4:
    pulled_number = choice(possibilities)

    if pulled_number not in winning_ticet:
        winning_ticet.append(pulled_number)

print(f"the winning ticket is {winning_ticet}")
