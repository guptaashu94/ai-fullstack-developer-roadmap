year = int(input("Enter a year: "))

if year % 400 == 0:
    print(f"{year} is a Leap Year.")
elif year % 100 == 0:
    print(f"{year} is not a Leap Year.")
elif year % 4 == 0:
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is not a Leap Year.")