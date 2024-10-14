# nesting quiz
# page 171

# 6-7
person_1= {
    'name': 'ahmed',
    'age': 30,
    'country': 'egypt',
    }

person_2 = {
    'name':'khaled',
    'age':32,
    'country':'africa',
    }

person_3 = {
    'name': 'ola',
    'age': '21',
    'country': 'usa',
    }

people =[person_1,person_2,person_3]

for person in people:
    print(f"{person['name']}, is {person['age']} years old and is from {person['country']}")


pet1= {
    'owner': 'ahmed',
    'pet type': 'dog',
    }

pet2= {
    'owner':'ola',
    'pet type': 'cat',
    }

pet3= {
    'owner': 'khaled',
    'pet type': 'fish',
    }

pets= [pet1,pet2,pet3]

for pet in pets:
    print(f"\n{pet['owner'].title()}, have a very cute {pet['pet type'].title()}")



favorite_places= {
    'ahmed': ['egypt','spain'],
    'ola': ['egypt','france'],
    'khaled': ['egypt','ras sudr','uae'],
    }

for name, place in favorite_places.items():
    print(f"Hi, {name.title()} your favorite places are: {place}, are there any other places to add?")
    new_place= input(f"Please enter your favorite place: ")
    if new_place.lower() == 'no':
        print(f"thank you, your favorite places are {place}")
    elif new_place.lower() in place:
        print(f"the place was already added")
        print(f"you favorite places are:{place}")
    elif new_place.lower() not in place:
        place.append(new_place)
        print(f"thank you{name.title()}, now your new favorite place list is:{place}")


favorite_numbers= {
    'ahmed': [1,3],
    'khaled': [5,9],
    'ola': [4],
    }

for name, favorite_numbers in favorite_numbers.items():
    print(f"\n{name.title()} favorite numbers are {favorite_numbers}")


# 6-11
cities= {
    'cairo': {
        'country':'egypt',
        'population': 110_000_000,
        'fact': 'oldest city in the world'
        },
    'tokya': {
        'country':'japan',
        'population': 50_000_000,
        'fact': "everyone like's it",
        },
    'paris': {
        'country': 'france',
        'population':20_000_000,
        'fact': 'great place to visit',
        }
}

for city_name,city_information in cities.items():
    print(f"\n{city_name.title()} is the city of {city_information.get('country').title()}, its population is "
          f"\n{city_information.get('population')}, fact about {city_name.title()}:\n{city_information.get('fact')}")

