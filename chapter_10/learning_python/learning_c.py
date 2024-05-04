from pathlib import Path

path = Path('learning_python.txt')

contents = path.read_text().rstrip().replace('Python', 'C')
lines = contents.splitlines()
for line in lines:
    print(line)

