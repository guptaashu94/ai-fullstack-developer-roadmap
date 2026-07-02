students = []

while True:
    print("\n" + "=" * 30)
    print(" Student Management System")
    print("=" * 30)
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        name = input("Enter student name: ").strip()

        if not name:
            print("Student name cannot be empty.")
            continue

        # Check for duplicate (case-insensitive)
        exists = False

        for student in students:
            if student.lower() == name.lower():
                exists = True
                break

        if exists:
            print(f'"{name}" already exists.')
        else:
            students.append(name)
            print(f'"{name}" added successfully.')

    elif choice == "2":

        if not students:
            print("\nNo students found.")
        else:
            print("\nStudent List")
            print("-" * 20)

            for index, student in enumerate(students, start=1):
                print(f"{index}. {student}")

    elif choice == "3":

        name = input("Enter student name to search: ").strip()

        found = False

        for index, student in enumerate(students, start=1):
            if student.lower() == name.lower():
                print(f'"{student}" found at position {index}.')
                found = True
                break

        if not found:
            print(f'"{name}" not found.')

    elif choice == "4":

        name = input("Enter student name to delete: ").strip()

        found = False

        for student in students:
            if student.lower() == name.lower():
                students.remove(student)
                print(f'"{student}" deleted successfully.')
                found = True
                break

        if not found:
            print(f'"{name}" not found.')

    elif choice == "5":

        print("\nExiting Student Management System...")
        print(f"Total Students : {len(students)}")
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select a number between 1 and 5.")