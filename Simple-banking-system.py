sign = input("Would you like to sign up for Bank? (yes, no) ")
if sign == "yes":
      name = input("What is your name? ")
else:
    exit()
while True:
    create_password = input("Please create a password that contains a minium of 4 letters: ")
    if len(create_password) >= 4:
         print("Creating Account..")
         break
    else:
         print("Password is too short. Try again.")

while True:
    login = input("Would you like to login to your account? (yes, no) ")
    if login == "yes":
        login_name = input("What is the name? ")
        if login_name == name:
            print("Correct")
            break
    elif login == "no":
        exit()
    else:
        print("Invalid. Try again.")
    
while True:
    login_password = input("What is the password to the account: ")
    if login_password == create_password:
        print("Correct.")
        print("Logging in...")
        break
    else:
        print("Incorrect.")

print()
print()

print(f"Welcome {name}")
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