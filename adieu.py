import sys

def main():
    print("Please enter names (Ctrl-D to end):")

    # Read all input names until EOF (Ctrl-D)
    try:
        names = sys.stdin.read().strip().split('\n')
    except EOFError:
        pass

    # Generate and print the farewell message
    farewell_message = generate_farewell(names)
    print(farewell_message)

def generate_farewell(names):
    if len(names) == 1:
        return f"Adieu, adieu, to {names[0]}"
    elif len(names) == 2:
        return f"Adieu, adieu, to {names[0]} and {names[1]}"
    else:
        all_but_last = ", ".join(names[:-1])
        last = names[-1]
        return f"Adieu, adieu, to {all_but_last}, and {last}"

if __name__ == "__main__":
    main()
