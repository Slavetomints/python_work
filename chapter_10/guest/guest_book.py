from pathlib import Path 

path = Path('guest.txt')


active = True
contents = ''

while active:
    name = input('Please enter your name, enter "quit" if you wish to exit: ')
    if name.lower() == 'quit':
        active = False
    else:
        contents += f'\n {name}'

path.write_text(contents)

