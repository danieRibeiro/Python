def name_city_country_population(city, country, population=False):
    if population:
        formatted_name = f'{city.title()}, {country.title()} - População: {population}'
    else:
        formatted_name = f'{city.title()}, {country.title()}.'.title()
    return formatted_name
