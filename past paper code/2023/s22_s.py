# Handwritten data for testing
Account=[
    ["Tom","123456"],
    ["Jerry","abcdef"],
    ["July","abc123"]
]
Accdetails=[
    # balance, overdraft, withdraw
    [250.00,100.00,200.0],
    [350.0,150.0,200.0],
    [450.0,200.0,250.0]
]
Size=3

# The code for answering the question
def checkMatch(accountID):
    # checks the Account ID exists
    if accountID >= Size or accountID <0:
        print("Account id not exist.")
        return False
    
    name=input("input your name:")
    passward=input("input your passward:")
    # check the name and password entered by the account holder match the name and password stored in Account[] 
    if name==Account[accountID][0] and passward==Account[accountID][1]:
        return True
    else:    
        print("Invalid name or password.")
        return False

def displayBalace(accountID):
    print("The balance is:",Accdetails[accountID][0])

def withDraw(accountID):
    money=float(input("input the withdraw money you want:"))
    # withdraw money should be less than or equal to withdraw limit
    if money <= Accdetails[accountID][2]:
        #  check withdraw money <= balance + overdraft limit
        if money <= Accdetails[accountID][0] + Accdetails[accountID][1]:
            Accdetails[accountID][0] = Accdetails[accountID][0] - money
            print("withdraw:",money)
        else:
            print("out of the sum of balance and overdraft")
    else:
        print("out of overdraft")

def deposit(accountID):
    amount=float(input("input the deposit:"))
    Accdetails[accountID][0]=Accdetails[accountID][0]+amount
    print("Deposit money:", amount)
    

accountID = int(input("Enter Account ID:"))

# check it before any action can take place
valid = checkMatch(accountID)
if valid:
    # a variable used to record whether the user has chosen to exit
    running = True
    while running:
        print("Menu:")
        print("1. display balance")
        print("2. withdraw money")
        print("3. deposit money")
        print("4. exit")
        choice = input("Choose menu by index(1,2,3,4):")
        # According to the user's choice, call the corresponding function or code
        if choice == "1":
            displayBalace(accountID)
        elif choice == "2":
            withDraw(accountID)
        elif choice == "3":
            deposit(accountID)
        elif choice == "4":
            running = False
        else:
            print("Invalid choice")
else:
    print("Invalid Account or name or password not match!")
