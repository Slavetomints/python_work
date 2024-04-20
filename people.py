people = {
    'alistair': {
        'first_name': 'alistair', 
        'last_name': 'petz', 
        'age': 16, 
        'city': 'rockton'
    },

    'daisy': {
        'first_name': 'daisy',
        'last_name': 'hardwick',
        'age': 18,
        'city': 'roscoe'
    },

    'calypso': {
        'first_name': 'calypso',
        'last_name': 'kramper',
        'age': 16,
        'city': 'rockton'
    },
}

for person, info in people.items():
    print(f'{person.title()}:')

    full_name = f"{info['first_name']} {info['last_name']}"
    age = info['age']
    city = info['city']

    print(f'\tFull name: {full_name.title()}')
    print(f'\tAge: {age}')
    print(f'\tCity: {city.title()}')