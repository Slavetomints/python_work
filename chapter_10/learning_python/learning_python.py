from pathlib import Path

path = Path('learning_python.txt')

contents = path.read_text().rstrip()
lines = contents.splitlines()
for line in lines:
    print(line)

print(contents)