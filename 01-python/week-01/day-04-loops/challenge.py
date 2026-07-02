# balance = 1000.0  # Initial balance
INITIAL_BALANCE = 1000.0
balance = INITIAL_BALANCE
transactions = 0
last_transaction = "No transactions yet."

while True:
    print("\n==========================")
    print("         ATM MENU")
    print("==========================")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(f"\nCurrent Balance: ₹{balance:.2f}")

    elif choice == "2":
        # amount = float(input("Enter deposit amount: ₹"))
        try:
            amount = float(input("Enter amount: ₹"))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if amount <= 0:
            print("Deposit amount must be greater than zero.")
        else:
            balance += amount
            transactions += 1
            last_transaction = f"Deposited ₹{amount:.2f}"
            print(f"Deposit successful!")
            print(f"Updated Balance: ₹{balance:.2f}")

    elif choice == "3":
        # amount = float(input("Enter withdrawal amount: ₹"))
        try:
            amount = float(input("Enter withdrawal amount: ₹"))
        except ValueError:
            print("Please enter a valid number.")
            continue
          
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            transactions += 1
            last_transaction = f"Withdrew ₹{amount:.2f}"
            print("Withdrawal successful!")
            print(f"Updated Balance: ₹{balance:.2f}")

    elif choice == "4":
        confirm = input("Are you sure you want to exit? (yes/no): ").lower()

        # if confirm == "yes":
        if confirm in ("y", "yes"):
            print("\n===== ATM Summary =====")
            print(f"Final Balance: ₹{balance:.2f}")
            print(f"Total Transactions: {transactions}")
            print(f"Last Transaction: {last_transaction}")
            print("Thank you for using our ATM!")
            break
        else:
            print("Returning to the ATM menu...")

    else:
        print("Invalid choice. Please select a number between 1 and 4.")