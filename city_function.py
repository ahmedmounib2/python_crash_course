def city_name_country(city, country, population = ''):
    """return the 'City, Country' . """
    if population:
        populationx = f"population: {population}"
        cityname = f"{city}, {country}, {populationx}"
    else:
        cityname = f"{city}, {country}"
    return cityname.title()

