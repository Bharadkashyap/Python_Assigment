def calculate(no1,no2,op):
    
    match op:
        case '+':
            print(f"Addition is:{no1+no2}")
        case '-':
            return no1-no2
        case '*':
            print(f"Multi is:{no1*no2}")
        case '/':
            print(f"Division is:{no1/no2}")
        case _:
            print(f"Invalid")


no1=int(input("Enter Number1:"))
no2=int(input("Enter Number2:"))
op=input("Enter Operation:")

print(calculate(no1,no2,op))
