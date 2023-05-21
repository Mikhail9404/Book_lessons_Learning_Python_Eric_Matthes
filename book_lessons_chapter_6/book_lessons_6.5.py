river_in_country = {
    'nile': 'egypt',
    'volga': 'russia',
    'amazonka': 'brazil',
}

for river, country in river_in_country.items():
    print(f'The {river.title()} runs through {country.title()}')

for river in river_in_country.keys():
    print(river.title())

for country in river_in_country.values():
    print(country.title())