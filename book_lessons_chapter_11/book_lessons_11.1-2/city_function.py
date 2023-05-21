def get_formatted_string_city_country(city, country, population=''):
    if population:
        formatted_string_city_country = f"{city}, {country} - population {population}"
    else:
        formatted_string_city_country = f"{city}, {country}"
    return formatted_string_city_country.title()

