# this is the class and the methods
class Budget:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self.balance

    def checkBalance(self):
        return self.balance


#this are the instance of the class
food = Budget(2000)
clothing = Budget(3000)
entertainment = Budget(500)


#this is a function to implement the transfer
def Transfer():
    count = 0
    check = True
    while (check == True):
        WhatToDo = int(input(
            "What Operation do you want to perform:\n1) Transfer from food to clothings Account  \n2) Transfer from food to entertainment Account \n3) Transfer from clothing to food Account \n4) Transfer from clothing to entertainment Account \n5) Transfer from entertainment to food Account \n6) Transfer from entertainment to clothings Account\n7) Exit Program \n0)Back \nType here: "))

        if WhatToDo == 1:
            amount = int(input("Enter your money: "))
            foodAcc = food.withdraw(amount)
            clothingAcc = clothing.deposit(amount)
            print(
                f'Your food Balance is now: GH₵{foodAcc} and your clothing Balance is: GH₵{clothingAcc}')
        elif WhatToDo == 2:
            amount = int(input("Enter your money: "))
            foodAcc = food.withdraw(amount)
            entertainmentAcc = entertainment.deposit(amount)
            print(
                f'Your food Balance is now: GH₵{foodAcc} and your clothing Balance is: GH₵{entertainmentAcc}')
        elif WhatToDo == 3:
            amount = int(input("Enter your money: "))
            clothingAcc = clothing.withdraw(amount)
            foodAcc = food.deposit(amount)
            print(
                f'Your food Balance is now: GH₵{clothingAcc} and your clothing Balance is: GH₵{foodAcc}')
        elif WhatToDo == 4:
            amount = int(input("Enter your money: "))
            clothingAcc = clothing.withdraw(amount)
            entertainmentAcc = entertainment.deposit(amount)
            print(
                f'Your food Balance is now: GH₵{clothingAcc} and your clothing Balance is: GH₵{entertainmentAcc}')
        elif WhatToDo == 5:
            amount = int(input("Enter your money: "))
            entertainmentAcc = entertainment.withdraw(amount)
            foodAcc = food.deposit(amount)
            print(
                f'Your food Balance is now: GH₵{entertainmentAcc} and your clothing Balance is: GH₵{foodAcc}')
        elif WhatToDo == 6:
            amount = int(input("Enter your money: "))
            entertainmentAcc = entertainment.withdraw(amount)
            clothingAcc = clothing.deposit(amount)
            print(
                f'Your food Balance is now: GH₵{entertainmentAcc} and your clothing Balance is: GH₵{clothingAcc}')
        elif (WhatToDo == 0):
            break
        elif(WhatToDo == 7):
            exit()
        else:
            print("Invalid Option!")
            count += 1
            if count == 3:
                print("Program returned to main menu\n")
                break


count = 0
check = True
print("\n\n==================================== Welcome to Bugeting System ====================================\n")
while (check == True):
    WhatToDo = int(
        input("\nWhat Operation do you want to perform:\n1) Deposit \n2) Withdraw \n3) Check Balance \n4) Transfers \n5) Exit Program\nType here: \n"))
    if (WhatToDo == 1):
        while (check == True):
            WhatToDo = int(input(
                "What Operation do you want to perform:\n1) Deposit to food Balance  \n2) Deposit to clothing Balance \n3) Deposit to entertainment Balance\n4) Exit Program\n0)Back\nType here:  "))
            if (WhatToDo == 1):
                amount = int(input("Enter your money: "))
                foodAcc = food.deposit(amount)
                print("Your Food balance is: GH₵", foodAcc)
            elif (WhatToDo == 2):
                amount = int(input("Enter your money: "))
                clothingAcc = clothing.deposit(amount)
                print("Your clothing balance is: GH₵", clothingAcc)
            elif (WhatToDo == 3):
                amount = int(input("Enter your money: "))
                entertainmentAcc = entertainment.deposit(amount)
                print("Your entertainment balance is: GH₵", entertainmentAcc)
            elif(WhatToDo == 0):
                break
            elif(WhatToDo == 4):
                exit()
            else:
                print("Invalid Option!")
                count += 1
                if count == 3:
                    print("Program returned to main menu\n")
                    break
            
            print("\n")

    elif (WhatToDo == 2):
        while (check == True):
            WhatToDo = int(input(
                "What Operation do you want to perform:\n1) Withdraw from food Balance  \n2) Withdraw from clothing Balance \n3) Withdraw from entertainment Balance\n4) Exit Program \n0) Back \nType here: "))
            if (WhatToDo == 1):
                amount = float(input("Enter your money: "))
                foodAcc = food.withdraw(amount)
                print("Your entertainment balance is: GH₵", foodAcc)
            elif (WhatToDo == 2):
                amount = float(input("Enter your money: "))
                clothingAcc = clothing.Withdraw(amount)
                print("Your entertainment balance is: GH₵", clothingAcc)
            elif (WhatToDo == 3):
                amount = float(input("Enter your money: "))
                entertainmentAcc = entertainment.Withdraw(amount)
                print("Your entertainment balance is: GH₵", entertainmentAcc)
            elif (WhatToDo == 0):
                break
            elif(WhatToDo == 4):
                exit()
            else:
                print("Invalid Option!")
                count += 1
                if count == 3:
                    print("Program returned to main menu\n")
                    break
            print("\n")

    elif (WhatToDo == 3):
        while (check == True):
            WhatToDo = int(input(
                "What Operation do you want to perform:\n1) Check food Balance  \n2) Check clothing Balance \n3) Check entertainment Balance\n4) Exit Program \n0) Back \nType here: "))
            if (WhatToDo == 1):
                foodAcc = food.checkBalance()
                print("Your food Balance is: GH₵", foodAcc)
            elif (WhatToDo == 2):
                clothingAcc = clothing.checkBalance()
                print("Your clothing Balance is: GH₵", clothingAcc)
            elif (WhatToDo == 3):
                entertainmentAcc = entertainment.checkBalance()
                print("Your entertainment Balance is: GH₵", entertainmentAcc)
            elif(WhatToDo == 0):
                break
            elif(WhatToDo == 4):
                exit()
            else:
                print("Invalid Option!")
                count += 1
                if count == 3:
                    print("Program returned to main menu\n")
                    break
            print("\n")

    elif (WhatToDo == 4):

        Transfer()
        print("\n")

    elif(WhatToDo == 5):
        break
    else:
        print("Invalid Option!")
        count += 1
        if count == 5:
            print("Program Aborted")
            break
