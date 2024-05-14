from pathlib import Path 

path = Path('guest.txt')

path.write_text(input('What is your name? '))