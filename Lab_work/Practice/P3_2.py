class Student:
    def AddStudent(self):
        self.RollNo = input("Enter Roll Number: ")
        self.Name = input("Enter Name: ")
        self.Age = input("Enter Age: ")
        self.Gender = input("Enter Gender: ")

    def DisplayStudent(self):
        print("\n--- Student Details ---")
        print("Roll No:", self.RollNo)
        print("Name:", self.Name)
        print("Age:", self.Age)
        print("Gender:", self.Gender)

# Example usage
s1 = Student()
s1.AddStudent()
s1.DisplayStudent()
