students = {}

while True:
    print("\nMenu:")
    print("a) Add Student")
    print("b) Search Student")
    print("c) List All Students")
    print("d) Update Student")
    print("e) Delete Student")
    print("f) Exit")

    choice = input("Enter choice: ")

    if choice == "a":
        roll = input("Enter roll number: ")
        name = input("Enter name: ")
        students[roll] = name
        print("Student added.")
    elif choice == "b":
        roll = input("Enter roll number to search: ")
        print("Found:", students.get(roll, "Not found"))
    elif choice == "c":
        print("All Students:", students)
    elif choice == "d":
        roll = input("Enter roll number to update: ")
        if roll in students:
            students[roll] = input("Enter new name: ")
            print("Updated successfully.")
        else:
            print("Student not found.")
    elif choice == "e":
        roll = input("Enter roll number to delete: ")
        if roll in students:
            del students[roll]
            print("Deleted successfully.")
        else:
            print("Student not found.")
    elif choice == "f":
        break
    else:
        print("Invalid choice.")
