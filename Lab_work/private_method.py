#06-03-2024
class computer:
    def __msg(self):
        print("hello Guys")
    def show(self):
        self.__msg()
c=computer()
c.show()

#error massage show
class Student:
    def show(self):
        print("hello")
s=Student()
del s #it throws Error
s.show
