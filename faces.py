# faces.py

def convert(text):
    """
    Convert emoticons in the input text to their corresponding emoji.

    :param text: str, input text containing emoticons
    :return: str, text with emoticons converted to emoji
    """
    # Replace emoticons with corresponding emojis
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    """
    Prompt the user for input, convert emoticons to emoji, and print the result.
    """
    # Prompt the user for input
    user_input = input("Enter your text: ")

    # Convert emoticons to emoji
    result = convert(user_input)

    # Print the result
    print(result)

if __name__ == "__main__":
    main()
