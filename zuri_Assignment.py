import time
import random


def withdral(amount, availableAmount):
    balance = availableAmount - amount
    return balance

def deposit(amount, availableAmount):
    balance = availableAmount + amount
    return balance

def complaint(message):
    print("your issue ",message, " will be solve for you")
    print("Thank you for contacting us")
    pass
def generateAccNumber():
    randomlist = []
    n = random.randint(1000000, 3000000)
    randomlist.append(n)
    return randomlist

allowedusers = ["kofi", "ama", "ernest"]
allowedpassword = ["1233", "pass", "ern12"]
accNumber = []
avalableAmount = 2000
ballance = 0

cont = False
while(cont == False):
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print("time: ",current_time)




    take = int(input("Press 1 to register a member or press 0 to login: "))

    if(take == 1):
         takeName = input("Enter the name: ")
         takePass = input("Enter password: ")
         allowedusers.append(takeName)
         allowedpassword.append(takePass)
         accNumber.append(generateAccNumber())
         print("The Account Number is: ", generateAccNumber())
    elif(take == 0):

        name = input("Enter your user name: ")

        if(name in allowedusers):
            password = input("enter your password: ")
            userid = allowedusers.index(name)

            if(password == allowedpassword[userid]):
                print("Welcome ", name)
                print("Available options to chose from")
                print(" 1. withdrawal \n 2.cash deposit \n 3. complaint")

                selectedOption = int(input("Please select an option: "))

                if (selectedOption == 1):
                    amount = int(input("How much would you like to withdraw: "))
                    if (amount >= avalableAmount):
                        print("you can not chash this amount!")
                    else:
                        ballance = withdral(amount, avalableAmount)
                        print("take your money ", amount, "your remaining balance is: ", ballance)
                elif(selectedOption == 2):
                    amount = int(input("How much would you like to deposit?"))
                    ballance = deposit(amount, avalableAmount)
                    print("you have deposit ", amount, "now your balance is: ", ballance)

                elif(selectedOption == 3):
                    message = input("What issue will you like to report? ")
                    complaint(message)

                else:
                    print("invalid option selected")
                    pass

                print(" succesfull ",)
            else:
                print("incorect password! ")
        else:
            print("neme not found! ")
    else:
        print("Please check your selection")
    use = input("Press y o continue: ")
    if(use == 'y'):
        cont = False
    else:
        cont = True


