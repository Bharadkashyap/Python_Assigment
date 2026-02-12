'''3. Function to Calculate Factorial (Using Recursion)
 Implement factorial using:
o Normal function
o Recursive function'''


#normal function of factorial
def fact1(n):
    if n<0:
        return "Invalid"
    if n==1 or n==0:
        return 1
    f=1
    for i in range(1,n+1):
         f*=i
    return f

#Recursion function
def fact1_rec(n):
    if n<0:
        return "Invalid"
    if n==1 or n==0:
        return 1
    else:
        return n*fact1_rec(n-1)

#Main Program
fact=int(input("Entre Factorial"))
fact_rec=int(input("Entre Factorial for 2nd"))
print("factorial is",fact1(fact))
print("factorial in recursion is",fact1_rec(fact_rec))
