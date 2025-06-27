def main():
    price = 50
    amount_due = price
    accepted_coins = [25, 10, 5]

    while amount_due > 0:
        print(f"Amount Due: {amount_due}\n")
        coin = int(input())

        if coin in accepted_coins:
            amount_due -= coin


    if amount_due < 0:
        change = abs(amount_due)
        print(f"Change Owed: {change}")
    else:
        print("Change Owed: 0")

if __name__ == "__main__":
    main()
