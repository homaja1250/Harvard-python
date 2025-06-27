import sys
import os
import csv
from tabulate import tabulate

def main():
    # Check if exactly one command-line argument is provided
    if len(sys.argv) != 2:
        print("Usage: python pizza.py <filename.csv>")
        sys.exit(1)

    # Get the file name from the command-line argument
    filename = sys.argv[1]

    # Check if the file name ends with .csv
    if not filename.endswith('.csv'):
        print("Error: The file must be a CSV.")
        sys.exit(1)

    # Check if the file exists
    if not os.path.isfile(filename):
        print(f"Error: The file '{filename}' does not exist.")
        sys.exit(1)

    # Read the CSV file
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            # Read the headers
            headers = next(reader)
            # Read the rest of the data
            data = [row for row in reader]
    except Exception as e:
        print(f"Error: Could not read the file '{filename}'. {e}")
        sys.exit(1)

    # Format the table using tabulate
    table = tabulate(data, headers=headers, tablefmt="grid")

    # Print the formatted table
    print(table)

if __name__ == "__main__":
    main()
