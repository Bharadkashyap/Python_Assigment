'''2. Function to Find Largest of Three Numbers
 Accept three numbers as parameters.
 Return the largest number.'''

def Large(a,b,c):
    if a>b  and a>c:
       return a
    elif b>a  and b>c:
        return b
    elif c>a  and c>b:
        return c
    else:
        print("All are Equals")

a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
c=int(input("Enter Third Number:"))
r=Large(a,b,c)

print(f"Large number is {r}")
