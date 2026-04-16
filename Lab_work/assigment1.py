#(1)Write a python program to print “Hello World!”

print("Hello World!")
#(2)Write a python program to take 2 numbers from the user and perform Arithmetic Operations.

a=int(input("enter a="))
b=int(input("enter b="))
sum=a+b;
print(sum)
s=a-b;
print(s)
mul=a*b;
print(mul)
div=a/b;
print(div)

#(3)Write a python program to calculate the area of a circle.

r=float(input("Enter number of circle="))
pi=3.14
s=pi*r*r
print("area of circle is=",s)

#(4) Write a python program to check whether the entered number is positive , negative or zero.

A=int(input("Enter number="))
if A==0:
    print("equalt to zero")
elif A>0:
    print("number is positoive")
else :
    print(" number is negative")


#(5) Write a Python program to calculate the length of a string.

s="kashyap"
print(len(s))

#(6) Write a python program to reverse a given string.

a="ATMIYA"
print(a[::-1])

#(7)Write a Python program that takes a list of words and returns the length of the list

S=["kashyap",123,10.5]
print(len(S))

#(8) Write a Python program to print the characters which have odd index values of a given string.
o="Atmiya university"
print(o[1::2])

#(9)Write a Python program to print the elements which have even index values of a given list.
o="Atmiya university"
print(o[0::2])

#(10)Write a python program to print the last element of a given list.
o=["Atmiya university",1,10.5]
print(o[-1])

#(11) Write a python program to find the factorial of a given number.
n=int(input("Enter number of factiorial="))
a=range(1,n+1)
fact=1
for i in  a:
    fact=fact*i
print(fact)

#(12)Write a python program to find out the sum of digits of a given number.
a=input("enter any number")
sum=0
for i in a:
    sum=sum+int(i)
print(sum)
    
#(13)Write a python program to find out the sum of odd and even numbers between a given range.

x=0
a=int(input("enter numbers="))
for i in range(0,a,2):
    x=x+i
print(x)

y=0
for i in range(1,a,2):
    y=y+i
print(y)
total=x+y
print("sum of even and oddnumbers=",total)


#(14)Write a python program which accepts the number one by one until the user enters 0. Find out total positive numbers, total negative numbers,average of the nos. and total numbers you entered.

n=None
pos_count=0
neg_count=0
no=[]
while n!=0:
    n=int(input("enter value:"))
    if n>0:
        pos_count+=1
    elif n<0:
        neg_count+=1
    else:
        break
    no.append(n)
print(no)
print("average",sum(no)/len(no))
print("positive",pos_count)
print("negative",neg_count)
print("total",len(no))


