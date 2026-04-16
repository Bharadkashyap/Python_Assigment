#21-02-2024
'''
#1.......
class Student:
    rno=0;
    name="";
    def getdata(self):
        self.rno=int(input("enter rollno="))
        self.name=input("enter name=")
    def display(self):
        print("your rollno is=",self.rno)
        print("your name is=",self.name)
s1=Student()
s1.getdata()
s1.display()
#2.....
class Uservalue:
    a=10
    def display(self):
        print(self.a)
u1=Uservalue()
u1.display()
#3.......constructor
class Stud:
    def __init__(self,nm=""):
        self.name=nm
        print("your name is=",self.name)
s1=Stud("kashyap")
#4.......Inheritance(single)
class University:
    def uname(self):
        print("Atmiya")
class department(University):
    def dept(self):
        print("CS&IT")
d1=department()
d1.uname()
d1.dept()
#5......inheritance(multilevel)
class University:
    def uname(self):
        print("Atmiya University")
class collage(University):
    def clg(self):
        print("Atmiya collage")
class department(collage):
    def dept(self):
        print("CS&IT")
d1=department()
d1.uname()
d1.clg()
d1.dept()
#5.....inheritance(multiple)
class Mother:
    def mname(self):
        print("sita")
        
class Father(Mother):
    def fname(self):
        print("Ram")

class Son(Father,Mother):
    def sname(self):
        print("luv&kush")
s1=Son()
s1.mname()
s1.fname()
s1.sname()

#6......inheritance(hierachical)
class Father:
    def fname(self):
        print("Ram")
        
class Son1(Father):
    def sname1(self):
        print("luv")

class Son2(Father):
    def sname2(self):
        print("kush")
s1=Son1()
s1.fname()
s1.sname1()

s2=Son2()
s2.fname()
s2.sname2()

#7.....inheritance(hybrid)
class Grandfather:
    def gname(self):
        print("Dashrath")
        
class Father(Grandfather):
    def fname(self):
        print("Ram")

class Son1(Father):
    def sname1(self):
        print("Luv")
class Son2(Father):
    def sname2(self):
        print("kush")

s1=Son1()
s1.gname()
s1.fname()
s1.sname1()

s2=Son2()
s2.gname()
s2.fname()
s2.sname2()'''











        
