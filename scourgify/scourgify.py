import sys
import os
import csv

if len(sys.argv) != 3:
    print("Usage: python scourgify.py input.csv output.csv")
    sys.exit(1)

input_filename = sys.argv[1]
output_filename = sys.argv[2]

if not os.path.isfile(input_filename):
    print(f"Could not read {input_filename}")
    sys.exit(1)

if not input_filename.endswith(".csv"):
    print("Not a CSV file")
    sys.exit(1)

try:
    # Read the input CSV file
    with open(input_filename, "r") as infile:
        reader = csv.DictReader(infile)
        table = []
        for row in reader:
            last, first = row["name"].split(", ")
            table.append({"first": first, "last": last, "house": row["house"]})

    # Write to the output CSV file
    with open(output_filename, "w", newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(table)

except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)
