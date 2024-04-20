favorite_places = {
    'cal': ['band room', 'toontown, disneyland'],
    'gael': [''],
    'grace': ['room', 'ocean'],
    'daisy': ['hononegah tech office', 'home', 'tesomas scout camp'],
    'katherine': ['paris, france', 'room', 'portillos', 'california', 'michigan'],
    'rose': [''],
}

for person, places in favorite_places.items():
    print(f'{person.title()}')
    for place in places:
        print(f'\t{place.title()}')