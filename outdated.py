months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    date_input = input("Date: ")

    # Try parsing the date in MM/DD/YYYY format
    try:
        month, day, year = date_input.split("/")
        month = int(month)
        day = int(day)
        year = int(year)
        if 1 <= month <= 12 and 1 <= day <= 31:
            print(f"{year:04d}-{month:02d}-{day:02d}")
            break
    except ValueError:
        pass

    # Try parsing the date in 'Month DD, YYYY' format
    try:
        month_name, day_year = date_input.split(" ", 1)
        day, year = day_year.split(", ")
        month = months.index(month_name) + 1
        day = int(day)
        year = int(year)
        if 1 <= month <= 12 and 1 <= day <= 31:
            print(f"{year:04d}-{month:02d}-{day:02d}")
            break
    except (ValueError, IndexError):
        pass

    print("Invalid date format. Please try again.")
