import sys
import random
import pyfiglet

def main():
    # Check command-line arguments
    if len(sys.argv) not in [1, 3]:
        sys.exit("Usage: figlet.py [-f FONT]")

    # Check if the user wants a specific font
    if len(sys.argv) == 3:
        if sys.argv[1] not in ["-f", "--font"]:
            sys.exit("Invalid option. Use -f or --font to specify a font.")
        font = sys.argv[2]
    else:
        font = None

    # Get the list of available fonts
    available_fonts = pyfiglet.FigletFont.getFonts()

    # Check if the specified font is available
    if font and font not in available_fonts:
        sys.exit(f"Font '{font}' not found. Please choose a valid font.")

    # Prompt the user for input
    text = input("Input: ")

    # Create a Figlet object
    if font:
        figlet = pyfiglet.Figlet(font=font)
    else:
        # Choose a random font
        figlet = pyfiglet.Figlet(font=random.choice(available_fonts))

    # Output the text in the desired font
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()
