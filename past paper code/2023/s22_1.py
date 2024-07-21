def checkMatch(accountID):
    return false

def displayBalace(accountID):
    pass 

def withDraw(accountID):
    pass

def deposit(accountID):
    pass
    
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
