# Define the menu
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total_cost = 0.0

try:
    while True:
        # Prompt for user input
        item = input("Enter an item: ").strip().title()  # Convert to title case

        if item in menu:
            total_cost += menu[item]
            print(f"${total_cost:.2f}")
        else:
            # Ignore input that isn't an item on the menu
            continue

except EOFError:
    pass  # End of input detected with control-d (EOF)

print(f"Total cost: ${total_cost:.2f}")
