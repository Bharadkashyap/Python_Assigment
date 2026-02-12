'''1. Write a Function to Perform Arithmetic Operations
 Create separate functions for addition,
subtraction, multiplication, and division.
 Call them based on user input.'''

#Defining function

def addition(a,b):
    return a+b    
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Main program 

print("Select operation:") 
print("1. Addition") 
print("2. Subtraction") 
print("3. Multiplication") 
print("4. Division")

#input from user
choice = input("Enter choice (1/2/3/4): ") 
num1 = float(input("Enter first number: ")) 
num2 = float(input("Enter second number: "))

#Main condition
if choice == '1':
    print(f"The result is: {addition(num1, num2)}")
        
elif choice == '2':
    print(f"The result is: {subtraction(num1, num2)}")

elif choice == '3':
    print(f"The result is: {multiplication(num1, num2)}")
     
elif choice == '4':
    print(f"The result is: {division(num1, num2)}")
else:
    print("Invalid input")
