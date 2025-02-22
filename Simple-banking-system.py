import sys

def Creating_Username():
# Signing up
    sign = input("Would you like to sign up for Bank? (yes, no) ")
    if sign == "yes":
        name = input("What is your name? ")
        return name
    else:
        sys.exit()

def Creating_Password():
# Creating Password
    while True:
        create_password = input("Please create a password that contains a minium of 4 letters: ")
        if len(create_password) >= 4:
            print("Creating Account..")
            return create_password
        else:
            print("Password is too short. Try again.")

def Username_Check(Username):
# Logging in (Username)
    while True:
        login = input("Would you like to login to your account? (yes, no) ")
        if login == "yes":
            login_name = input("What is the name? ")
            if login_name == Username:
                print("Correct")
                break
        elif login == "no":
            sys.exit()
        else:
            print("Invalid. Try again.")

def Password_Check(Password):
# Logging in (Password)
    while True:
        login_password = input("What is the password to the account: ")
        if login_password == Password:
            print("Correct.")
            print("Logging in...")
            break
        else:
            print("Incorrect.")

def Bank_Account(Username):
# Bank Account
    print()
    print()

    print(f"Welcome {Username}")
    print()

    money = 0
    while True:
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        options = input("select one of the following numbers (1, 2, 3, 4) ")
        print()

        if options == "1":
            print(f"Your balance is £{money}")

        elif options == "2":
            depositStr = input("Pick a number to deposit some money: ")
            if depositStr.isdigit():
                deposit = int(depositStr)
                money = money + deposit
                print(f"You have deposited £{deposit}")
            else:
                print("Invalid")

        elif options == "3":
            withdrawStr = input("Pick a number to withdraw some money: ")
            if withdrawStr.isdigit():
                withdraw = int(withdrawStr)
                if money >= withdraw:
                    money = money - withdraw
                    print(f"You have withdrawn £{withdraw}")
                else:
                    print("You do not have enough.")    
            else:
                print("Invalid")

        elif options == "4":
            print("Goodbye :( ")
            break

#Game Execution
Username = Creating_Username()
Password = Creating_Password()
Username_Check(Username)
Password_Check(Password)
Bank_Account(Username)
