students = {}

while True:
    print("\n--- Student Grade System ---")
    print("1. Add Student")
    print("2. Update Grade")
    print("3. Show All Students")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        students[name] = grade
        print("Student added successfully!")

    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print("Grade updated successfully!")
        else:
            print("Student not found!")

    elif choice == "3":
        print("\n--- Student List ---")
        if not students:
            print("No students found")
        else:
            for name, grade in students.items():
                print(name, ":", grade)

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice, try again!")


