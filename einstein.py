# Define the speed of light in meters per second
SPEED_OF_LIGHT = 300000000  # 300 million meters per second

def main():
    # Prompt the user to input mass as an integer in kilograms
    mass = int(input("m: "))

    # Calculate energy using Einstein's formula E = mc^2
    energy = mass * SPEED_OF_LIGHT ** 2

    # Output the result as an integer
    print(f"{energy}")

if __name__ == "__main__":
    main()
