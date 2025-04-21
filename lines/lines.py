import sys
import os

valid_lines = 0

if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)

filename = sys.argv[1]

if not os.path.isfile(filename):
    print("File does not exist")
    sys.exit(1)

if not filename.endswith('.py'):
    print("Not a Python file")
    sys.exit(1)

try:
    with open(filename, 'r') as file:
        for line in file:
            stripped_line = line.strip()
            if stripped_line and not stripped_line.startswith('#'):
                valid_lines += 1
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)

print(valid_lines)
