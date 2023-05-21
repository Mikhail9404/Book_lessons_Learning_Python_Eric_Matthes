person_1 = {
    'first_name': 'Mikhail',
    'last_name': 'Kuznetsov',
    'age': '29',
    'city': 'St. Petersburg',
}

person_2 = {
    'first_name': 'Kristof',
    'last_name': 'Ben',
    'age': '34',
    'city': 'London',
}

person_3 = {
    'first_name': 'Bill',
    'last_name': 'Pollon',
    'age': '24',
    'city': 'New York',
}

people = [person_1, person_2, person_3]

for person_number in people:
    print(f'{person_number}\n')
    for character, info in person_number.items():
        print(f'{character.title()}: {info.title()}')
