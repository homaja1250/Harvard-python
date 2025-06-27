
import emoji

def emojize_string(input_string):
    return emoji.emojize(input_string, language='alias')

def main():
    user_input = input("Input: ")
    emojized_output = emojize_string(user_input)
    print("Output:", emojized_output)

if __name__ == "__main__":
    main()
