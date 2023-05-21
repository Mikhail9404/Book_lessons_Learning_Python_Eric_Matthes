Ben = {
        'kind of pet': 'dog',
        'pet owner': 'Mikle',
    }
Dick = {
        'kind of pet': 'cat',
        'pet owner': 'Boris',
    }
Loki = {
        'kind of pet': 'turtle',
        'pet owner': 'Brues',
    }
Pipi = {
        'kind of pet': 'mouse',
        'pet owner': 'Popug',
    }

pets = [Ben, Dick, Loki, Pipi]

for pet in pets:
    print(f'\n')
    for character, info in pet.items():
        print(f'{character.title()}: {info.title()}')