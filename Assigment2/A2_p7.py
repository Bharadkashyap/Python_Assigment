'''
give me in basic ok in python 7. Menu Driven Program: Student Result
System
Operations:
 Enter Marks
 Calculate Percentage
 Assign Grade
'''
marks = []

def enter_marks():
    global marks
    marks = []
    n = int(input("Enter number of subjects: "))
    for i in range(n):
        m = int(input("Enter marks of subject " + str(i+1) + ": "))
        marks.append(m)

def calculate_percentage():
    if len(marks) == 0:
        print("Please enter marks first.")
        return None
    total = sum(marks)
    percentage = total / len(marks)
    print("Percentage =", percentage)
    return percentage

def assign_grade():
    percentage = calculate_percentage()
    if percentage is None:
        return
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"
    print("Grade =", grade)

while True:
    print("\n--- Student Result System ---")
    print("1. Enter Marks")
    print("2. Calculate Percentage")
    print("3. Assign Grade")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        enter_marks()
    elif choice == 2:
        calculate_percentage()
    elif choice == 3:
        assign_grade()
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")
