#06-03-2024
"""
try:
    print("hello guys")
    print(x) # it throws Error
except:
    print("something went wrong")
else:
    print("NOthing Wrong")

#without error
x=10
try:
    print("hello guys")
    print(x)
except:
    print("something went wrong")
finally:
    print("this code is run if exception is raise or not ")

#TypeError:
a=int(input("Enetr number="))
b=input("Enetr number=")
try:
    sub=a-b;
    print("sub=",sub)
except TypeError:
    print("invalid inputs contact developers")


#ZeroDivisionError
a=int(input("Enetr number="))
b=int(input("Enetr number="))
try:
    d=a/b;
    print("div=",d)
except ZeroDivisionError:
    print("invalid division  contact developers")

#ValueError

try:
    a=int(input("Enetr number="))
    b=int(input("Enetr number="))
    d=a-b;
    print("sub=",d)
except ValueError:
    print("invalid inputs  contact developers")

#NameError
try:
    a=int(input("Enetr number="))
    d=a-b;
    print("sub=",d)
except NameError:
    print("invalid second inputs  contact developers")

#IndexError
a=[1,2,3]
print(a)
try:
    print(a[3])
except IndexError:
    print("invalid index")

   """
#User defined error
x=int(input("Enetr age="))

try:
    if x < 0:
        raise Exception
    else:
        print("valid age ")
except:
    print("Error less than 0")






