'''4. Function with Default Arguments
 Write a function to calculate simple interest.
 Keep rate default as 5%.'''

def sim(p,y,r=5):
    si=(p*r*y)/100
    return si

p=float(input("Enter Principal Amount"))
y=float(input("Enter years "))
r=float(input("Enter Rate of interest "))
print("Simple interest is:",sim(p,y,r))
