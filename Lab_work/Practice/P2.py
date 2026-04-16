#.Write a program to input 2 numbers and one arithmetic operator. Perform 
#operations as per arithmetic operator which is given as input

no1=int(input("Enter Number1:"))
no2=int(input("Enter Number2:"))
op=input("Enter Operation:")

match op:
    case '+':
        print(f"Addition is:{no1+no2}")
    case '-':
        print(f"Substraction is:{no1-no2}")
    case '*':
        print(f"Multi is:{no1*no2}")
    case '/':
        print(f"Division is:{no1/no2}")
    case _:
        print(f"Invalid")


        
