university="ABC"
class  Student:
     def __init__(self,rollno,name,gender,age):
         self.rollno=rollno
         self.name=name
         self.gender=gender
         self.age=age
     def display(self):
         print(self.rollno)
         print(self.name)
         print(self.gender)
         print(self.age)
         print(university)
class  course(Student):
    def __init__(self,rollno,name,gender,age,dept):
        super().__init__(rollno,name,gender,age)
        self.dept=dept
    def display1(self):
        super().display()
        print(self.dept)
    
    
c1=course(101,"kashyap","Male",21,"MCA")
c1.display1()
