cities = {
    'Moscow': {
        'country': 'Russia',
        'population': '11 980 000',
        'fact': 'It is based on the medieval fortress of the Kremlin.',
    },
    'London': {
        'country': 'England',
        'population': '8 982 000',
        'fact': 'In the heart of London is the Houses of Parliament - the Palace of Westminster.',
    },
    'Berlin': {
        'country': 'Germany',
        'population': '3 645 000',
        'fact': 'The city is famous for its art galleries and modern landmarks.',
    },
}
print(f'\nНиже представлен список городов и информация о каждом из них.')
for city, info in cities.items():
    print(f'\n{city}:')
    for keys, info_detailed in info.items():
        print(f'\t{keys.title()}: {info_detailed}')



