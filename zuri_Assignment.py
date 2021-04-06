import datetime
import random

AccountInfo = {}
balance = 200.0

def Time():
    x = datetime.datetime.now()
    print(x)

def init():
    Time()
    ValidSelected = False
    while ValidSelected == False:
        ValidSelected = True
        print("Hello welcome to banking system")
        HaveAcc = int(input("Do you have account 1 for Yes, 2 for No: "))
        if (HaveAcc == 1):
            login()

        elif (HaveAcc == 2):
            register()

        else:
            print("Invalid Selection")
            ValidSelected = False


def GenerateAccNumber():
    num = random.randint(1000000000, 9999999999)
    print("The Account Number is: ", num)
    return num


def withdral(amount, availableAmount,user):
    balance = availableAmount - amount
    print(user[0], user[1], "your current balance is: ", balance, "\n")
    accept = input("do you want to continue the system y / n: ")
    if (accept == 'y'):
        Operation(user)
    else:
        login()
    return balance


def deposit(amount, availableAmount, user):
    balance = availableAmount + amount
    print(user[0], user[1], "your current balance is: ", balance, "\n")
    accept = input("do you want to continue the system y / n: ")
    if (accept == 'y'):
        Operation(user)
    else:
        login()
    return balance


def complaint(message):
    print("your issue ", message, " will be solve for you")
    print("Thank you for contacting us")

    pass


def login():
    isLoginSuccessful = False

    while isLoginSuccessful == False:
        AccountNum = int(input("Enter your account Number: "))
        AccPassword = input("Enter your password: ")
        for AccountNumber, userDetails in AccountInfo.items():
            if (AccountNumber == AccountNum):
                if (userDetails[3] == AccPassword):
                    isLoginSuccessful = True
                    Operation(userDetails)
                else:
                    print("Invalid Login!")
            else:
                print("Invalid Login!")

    pass


def register():
    FName = input("Enter your first name: ")
    LName = input("Enter your last name: ")
    Email = input("Enter your Email: ")
    Password = input("Enter your password: ")
    AccountNumber = GenerateAccNumber()
    print("Account registration succesful")
    AccountInfo[AccountNumber] = [FName, LName, Email, Password]
    login()


def Operation(details):
    print("Welcom ", details[0],details[1])
    selection =int(input("Select an option \n1. Withdrawal \n2. Deposit \n3. Complaint \n4. logout \n5. Exit\nMake a choice: "))
    if(selection == 1):
        amount = int(input("Enter Amount to withdraw: "))
        withdral(amount,balance, details)
    elif(selection == 2):
        amount = int(input("Enter Amount to Deposit: "))
        deposit(amount, balance,details)
    elif (selection == 3):
        message = input("Enter your complain: \n")
        complaint(message)
    elif (selection == 4):
        login()
    elif (selection == 5):
        accept = input("do you want to exit the system y / n: ")
        if(accept == 'y'):
            exit()
        else:
            Operation(details)



init()
