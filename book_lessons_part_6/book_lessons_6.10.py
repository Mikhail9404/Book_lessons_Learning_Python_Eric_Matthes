favorite_numbers = {
    'Ben': [7, 10],
    'Ken': [29, 36, 18],
    'Vika': [69],
    'Sam': [4],
    'Petr': [8, 15],
}

for name, numbers in favorite_numbers.items():
    if len(numbers) > 1:
        print(f'Favorite numbers for {name.title()} are:')
        for number in numbers:
            print(f'\t{number}')
    else:
        for number in numbers:
            print(f'Favorite number for {name.title()} is {number}')