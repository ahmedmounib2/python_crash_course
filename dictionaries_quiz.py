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
