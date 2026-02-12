'''6. Banking System Using Functions
 Functions for:
o Deposit
o Withdraw
o Check Balance'''

#init
bal=1000.0

#dep
def dep(bal,amt):
    bal=bal+amt
    print("Amt deposited")
    return bal

def withdraw(bal,amt):
    if amt> bal:
        print("insuficient")
    else:
        bal-=amt
        print("Withdraw succesfully")
    return bal


def check(bal):
    print("Current balance is:",bal)

while True:
    print("1.deposite\n2.Withdraw\n3.Check\n4.exit")
    ch=int(input("Enter Choice:"))
    if ch==1:
        dep()
dep()
withdraw()
check()
