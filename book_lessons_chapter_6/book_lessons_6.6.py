favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

people_in_vote = ['sarah', 'bil', 'ann', 'edward']

for people in people_in_vote:
    if people in favorite_languages.keys():
        print(f'{people.title()}, thank you for your vote!')
    else:
        print(f'{people.title()}, please chose your prediction!')