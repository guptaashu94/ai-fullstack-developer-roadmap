number = int(input("Enter a number: "))

print(f"\nMultiplication Table of {number}")

for i in range(1, 11):
    print(f"{number} × {i} = {number * i}")