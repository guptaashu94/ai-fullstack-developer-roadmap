balance = 5000
daily_limit = 10000

amount = float(input("Enter withdrawal amount: ₹"))

if amount <= 0:
    print("Invalid amount! Please enter an amount greater than ₹0.")

elif amount > daily_limit:
    print(f"Daily withdrawal limit exceeded! Maximum allowed is ₹{daily_limit}.")

elif amount > balance:
    print("Insufficient balance!")

else:
    balance -= amount
    print("\n===== ATM Receipt =====")
    print("Withdrawal Successful!")
    print(f"Withdrawn Amount : ₹{amount:.2f}")
    print(f"Remaining Balance: ₹{balance:.2f}")