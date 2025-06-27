from collections import defaultdict

# Dictionary to store item counts
item_counts = defaultdict(int)

try:
    while True:
        # Prompt for user input
        item = input().strip().lower()  # Convert to lowercase

        if item:
            item_counts[item] += 1

except EOFError:
    pass  # End of input detected with control-d (EOF)

# Sort items alphabetically
sorted_items = sorted(item_counts.items())

# Print the grocery list
for item, count in sorted_items:
    print(f"{count} {item.upper()}")
