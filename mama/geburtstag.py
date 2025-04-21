import sys
import os
from tabulate import tabulate
import csv

if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)

filename = sys.argv[1]

if not os.path.isfile(filename):
    print("Not a CSV file")
    sys.exit(1)

if not filename.endswith(".csv"):
    print("Not a CSV file")
    sys.exit(1)

try:
    with open(filename, "r") as file:
        reader = csv.reader(file)
        table = list(reader)
        print(tabulate(table, headers="firstrow", tablefmt="grid"))
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)
