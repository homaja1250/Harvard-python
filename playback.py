# playback.py

def slow_speech():
    # Prompt the user for input
    user_input = input("Enter your text: ")

    # Replace each space with "..."
    slowed_down_input = user_input.replace(" ", "...")

    # Output the modified text
    print(slowed_down_input)

if __name__ == "__main__":
    slow_speech()
