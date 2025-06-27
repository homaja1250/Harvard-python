import sys
import os

def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        code_lines = 0
        for line in lines:
            stripped_line = line.strip()
            if stripped_line and not stripped_line.startswith('#'):
                code_lines += 1

        return code_lines
    except FileNotFoundError:
        sys.exit("File does not exist")

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python lines.py filename.py")

    filename = sys.argv[1]

    if not filename.endswith('.py'):
        sys.exit("Not a Python file")

    code_lines = count_lines(filename)
    print(code_lines)

if __name__ == "__main__":
    main()
