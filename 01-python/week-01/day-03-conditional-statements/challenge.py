employee_name = input("Enter employee name: ")
salary = float(input("Enter salary: ₹"))
experience = float(input("Enter years of experience: "))
performance = input("Performance (Excellent/Good/Average): ").strip().lower()

# Experience Bonus
if experience < 2:
    bonus_percentage = 5
elif experience <= 5:
    bonus_percentage = 10
else:
    bonus_percentage = 20

# Performance Bonus
if performance == "excellent":
    bonus_percentage += 5
elif performance == "good":
    bonus_percentage += 2
elif performance == "average":
    bonus_percentage += 0
else:
    print("Invalid performance rating.")
    exit()

bonus = salary * (bonus_percentage / 100)
net_salary = salary + bonus

print("\n=========================")
print("Employee Bonus Report")
print("=========================\n")

print(f"Employee    : {employee_name}")
print(f"Salary      : ₹{salary:,.2f}")
print(f"Experience  : {experience} Years")
print(f"Performance : {performance.title()}\n")

print(f"Bonus (%)   : {bonus_percentage}%")
print(f"Bonus       : ₹{bonus:,.2f}")
print(f"Net Salary  : ₹{net_salary:,.2f}")