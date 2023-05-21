favorite_places = {
    'Red Square': ['tom', 'mikle', 'tomas'],
    'Big Ben': ['tomas', 'kate'],
    'Savior on Spilled Blood': ['tomas', 'kate']
}

for place, names in favorite_places.items():
        print(f'\n{place.title()} is favorite place for:')
        for name in names:
            print(f'\t{name.title()}')
