name = input("Student Name: ")

english = int(input("English: "))
maths = int(input("Maths: "))
science = int(input("Science: "))

total = english + maths + science
percentage = total / 3

if percentage >= 90:
    grade = "A"
    passed = "Yes"
    distinction = "Yes"
    firstDivision = "Yes"
elif percentage >= 75:
    grade = "B"
    passed = "Yes"
    distinction = "No"
    firstDivision = "Yes"
elif percentage >= 60:
    grade = "C"
    passed = "Yes"
    distinction = "No"
    firstDivision = "Yes"
elif percentage >= 40:
    grade = "D"
    passed = "Yes"
    distinction = "No"
    firstDivision = "No"
else:
    grade = "Fail"
    passed = "No"
    distinction = "No"
    firstDivision = "No"

print("\n===== Report Card =====")
print(f"Student    : {name}")
print(f"Total      : {total}")
print(f"Percentage : {percentage:.2f}%")
print(f"Grade      : {grade}")
print(f"Pass : {passed}")
print(f"Distinction : {distinction}")
print(f"First Division : {firstDivision}")