#dictionaries quiz tests
# excercise 6-7 page 171

person_1 = {
    'first':'Ahmed',
    'last': 'monib',
    'location': 'egypt',
    }

person_2 = {
    'first': 'khaled',
    'last': 'monib',
    'location': 'cairo',
    }

person_3 = {
    'first': 'ola',
    'last': 'monib',
    'location': 'egypt',
    }

people = [person_1,person_2,person_3]


for person in people:
    firstname = person.get('first')
    lastname= person.get('last')
    location = person.get('location')
    print(f" {firstname.title()} {lastname.title()} is from {location.title()}")

pet1 = {
    'owner': 'ahmed',
    'pet': 'dog',
    }

pet2 = {
    'owner':'khaled',
    'pet': 'cat',
    }

pet3 = {
    'owner':'ola',
    'pet': 'lion',
    }

pets = [pet1,pet2,pet3]

for pet in pets:
    owner= pet.get('owner')
    pettype= pet.get('pet')
    print(f"\n{owner.title()} owns a pet {pettype}")

favorite_places= {
    'ahmed':['london','egypt','paris'],
    'ola': ['egypt','spain'],
    'khaled': ['zanzibar', 'egypt'],
    'eman': ['egypt','turkey']
    }

for name,places in favorite_places.items():
    extra_fav_places= input(f"Hi {name.title()} any other favorite places to add? ")
    if extra_fav_places.lower() == 'no':
        print(f"{name.title()}'s favorite places are {places}")
    elif extra_fav_places.lower() in places:
        print("this place was added already")
        print(f"{name.title()}'s favorite places are {places}")
    elif extra_fav_places.lower() not in places:
        places.append(extra_fav_places.lower())
        print(f"{name.title()}'s favorite places are {places}")


favorite_numbers= {
    'ahmed': [1,2],
    'ola':[2,6],
    'khaled': [5],
    }
for name, number in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are {number}")

cities= {
    'cairo': {
        'country':'egypt',
        'popuation':110_000_000,
        'fact': 'oldest city in the world'
        },
    'tokya': {
        'country':'japan',
        'population': 50_000_000,
        'fact': "everyone like's japan",
        },
    'paris': {
        'country': 'france',
        'population':20_000_000,
        'fact': 'great place to visit',
        }
}

for city_name,city_information in cities.items():
    print(f"{city_name} is the country {city_information[population]}")
