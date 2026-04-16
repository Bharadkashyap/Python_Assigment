"""
Write a program to create a list and perform various operations on list 
using menu.
"""

a=[]
aa=0
while True:
    op=int(input("Enter chose 1.create and addn2.update\n3.delete\n4.exit\n5.Display"))
    match op:
        case 1:
            n=int(input("Enter size"))
            for i in range(n):
                aa=int(input("Enter Value"))
                a.append(aa)
        case 2:
            n=int(input("Enter Index"))
            v=int(input("Enter Value"))
            a[n]=v
        case 3:
            v=int(input("Enter Value"))
            a.remove(v)
        case 4:
            print("Exiting")
            break
    
        case 5:
            for i in a:
                print(i)
        case _:
            print("invalid")
        
        
