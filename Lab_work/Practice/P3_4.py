class University:
    def __init__(self, uni_name):
        self.uni_name = uni_name
        self.department = self.Department("Computer Science")

    def show_university(self):
        print("University:", self.uni_name)

    class Department:
        def __init__(self, dept_name):
            self.dept_name = dept_name

        def show_department(self):
            print("Department:", self.dept_name)

# Usage
u = University("ABC University")
u.show_university()
u.department.show_department()
