import sys
import csv
import os

def main():
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python scourgify.py input.csv output.csv")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the input file exists
    if not os.path.isfile(input_file):
        print(f"Error: The file '{input_file}' does not exist.")
        sys.exit(1)

    try:
        # Read the input CSV file
        with open(input_file, 'r', newline='') as infile:
            reader = csv.DictReader(infile)
            students = []

            for row in reader:
                # Split the name into first and last name
                last, first = row['name'].split(', ')
                house = row['house']
                students.append({'first': first, 'last': last, 'house': house})

        # Write to the output CSV file
        with open(output_file, 'w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=['first', 'last', 'house'])
            writer.writeheader()
            writer.writerows(students)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
