from datetime import datetime

birth = int(input("Enter your birth year: "))

age = datetime.now().year - birth

print("Your age is:", age)