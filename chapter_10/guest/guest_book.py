from pathlib import Path 

path = Path('guest.txt')

active = True
names = []

while active:
    name = input('Please enter your name, enter "quit" if you wish to exit: ')
    if name.lower() == 'quit':
        active = False
    else:
        names.append(name)
# this is the only one i cant figure out

with open(path, 'w') as file:
    for name in names:
        file.write(f'{name}\n')
