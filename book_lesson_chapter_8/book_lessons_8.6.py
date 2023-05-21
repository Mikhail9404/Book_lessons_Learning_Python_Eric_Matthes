def city_country(city, country):
    formatted_city_country = f"{city}, {country}"
    return formatted_city_country.title()

print(city_country('сочи', 'россия'))
print(city_country('нью-йорк', 'америка'))
print(city_country('лондон', 'великобритания'))