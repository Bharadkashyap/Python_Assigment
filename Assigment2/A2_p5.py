'''5. Write a function inside another function.'''

def calculation(a,b):
    def add():
        return a+b
    def mul():
        return a*b
    print("Add is",add())
    print("Mul is:",mul())
    print("outer function is this")


a=int(input("Entre First number"))
b=int(input("Entre Second number"))
calculation(a,b)# call it here

