""".Write a program to enter marks of 4 subjects and display result (result 
shall include total, percentage and grade)"""

no1=int(input("Enter Number1:"))
no2=int(input("Enter Number2:"))

no3=int(input("Enter Number1:"))
no4=int(input("Enter Number2:"))
tot=no1+no2+no3+no4

per=(tot/400)*100

if per >=90:
    print("Grade A+")
elif per >=40 and per<90:
    print("Grade A")
else:
    print("Fail")

print(f"TOtal is:{tot}")
print(f"Percentage:{per}")    
