balance = 5000

amount = float(input("Enter withdrawal amount: "))

if amount <= balance:
    balance -= amount
    print(f"Withdrawal successful.")
    print(f"Remaining balance: ₹{balance:.2f}")
else:
    print("Insufficient balance.")