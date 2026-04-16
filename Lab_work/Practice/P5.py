"""
Write a program to enter 10 numbers and display largest odd number 
from the entered number.
"""

a=[]
aa=0
for i in range(10):
    aa=int(input("Enter Value"))
    a.append(aa)
l=None

for num in a:
    if num%2!=0:
        if l is None or num>l:
            l=num
if l is not None:
    print(l)
else:
    print("No Odd")
            
    
