name = input("Student Name: ")

english = int(input("English: "))
maths = int(input("Maths: "))
science = int(input("Science: "))

total = english + maths + science
percentage = total / 3

if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "Fail"

print("\n===== Report Card =====")
print(f"Student    : {name}")
print(f"Total      : {total}")
print(f"Percentage : {percentage:.2f}%")
print(f"Grade      : {grade}")