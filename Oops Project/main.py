import json
import random
import string
from pathlib import Path

class Bank:
    
    #class variable
    DbPath = 'db.json'
    __accountNumber = 0

    #constructor
    def __init__(self):
        self.data = []
        try:
            if Path(Bank.DbPath).exists():
                with open(Bank.DbPath) as fs:
                    self.data = json.load(fs)
            else:
                print("No such File Exist")
        except Exception as err:
            print(f"An error occurred: {err}")

    #instance method
    #create account
    def createAccount(self):
        try:
            UserInfo = {
                "name" : input("Tell your name : "),
                "age" : int(input("Tell your age : ")),
                "email" : input("Tell your email : "),
                "account_number" : Bank.__accountNumberGenerate(),
                "pin" : int(input("Create your pin : ")),
                "balance" : 0
            }

            if(UserInfo['age'] < 18):
                print("You are not eligible for creating account")
                return
            
            if(len(str(UserInfo['pin'])) < 4 ):
                print("Pin must be 4 digit")
                return
            
            self.data.append(UserInfo)
            self.__update()

            print("Account Created Successfully")
            
            for i in UserInfo:
                print(f"{i} : {UserInfo[i]}")
            print("Please note down you account number")
        except Exception as err:
            print(f"An error occurred: {err}")

    #deposit
    def deposit(self):
        try:
            account_number = input("Enter your account number : ")
            pin = int(input("Enter your pin : "))

            userData = [i for i in self.data if i['account_number'] == account_number and i['pin'] == pin]
            
            if not userData:
                print("Invalid account number or pin")
                return
            
            amount = int(input("Enter the amount to deposit : "))
            
            if amount <= 0 or amount > 10000:
                print("Sorry you can't deposit more than 10000 or less than 0")
                return
            
            userData[0]['balance'] += amount
            self.__update()
            print(f"Deposit successful. New balance: {userData[0]['balance']}")
        except Exception as err:
            print(f"An error occurred: {err}")

    #withdraw
    def withdraw(self):
        try:
            account_number = input("Enter your account number : ")
            pin = int(input("Enter your pin : "))

            userData = [i for i in self.data if i['account_number'] == account_number and i['pin'] == pin]

            if not userData:
                print("Invalid account number or pin")
                return
            
            amount = int(input("Enter the amount to withdraw : "))
            
            if amount <= 0 or amount > userData[0]['balance']:
                print("Sorry you can't withdraw more than your balance or less than 0")
                return
            
            if amount < 500:
                print("Sorry you can't withdraw less than 500")
                return
            
            userData[0]['balance'] -= amount
            self.__update()
            print(f"Withdraw successful. New balance: {userData[0]['balance']}")
        except Exception as err:
            print(f"An error occurred: {err}")

    #details
    def details(self):
        try:
            account_number = input("Enter your account number : ")
            pin = int(input("Enter your pin : "))

            userData = [i for i in self.data if i['account_number'] == account_number and i['pin'] == pin]

            if not userData:
                print("Invalid account number or pin")
                return
            
            print("Account Details")
            print("="*50)
            for i in userData[0]:
                if i == 'pin':
                    continue
                print(f"{i} : {userData[0][i]}")
            print("="*50)
        except Exception as err:
            print(f"An error occurred: {err}")

    #update
    def update(self):
        try:
            account_number = input("Enter your account number : ")
            pin = int(input("Enter your pin : "))

            userData = [i for i in self.data if i['account_number'] == account_number and i['pin'] == pin]

            if not userData:
                print("Invalid account number or pin")
                return
            print("You cannot update age , account number and balance")
            print("Fill the details for change or leave it empty if you don't want to change")
            new_data = {
                "name" : input("Enter your name : "),
                "email" : input("Enter your email : "),
                "pin" : int(input("Enter your pin : ")) if input("Do you want to change your pin? (y/n) : ") == 'y' else userData[0]['pin']
            }

            if new_data['name'] == '':
                new_data['name'] = userData[0]['name']
            
            if new_data['email'] == '':
                new_data['email'] = userData[0]['email']
            
            if new_data['pin'] != userData[0]['pin']:
                if len(str(new_data['pin'])) < 4:
                    print("Pin must be 4 digit")
                    return
                userData[0]['pin'] = new_data['pin']

            new_data['account_number'] = userData[0]['account_number']
            new_data['age'] = userData[0]['age']
            new_data['balance'] = userData[0]['balance']

            for i in new_data:
                if new_data[i] == userData[0][i]:
                    continue
                userData[0][i] = new_data[i]
                
            self.__update()
            print("Account updated successfully")
                
        except Exception as err:
            print(f"An error occurred: {err}")

    #delete account
    def delete(self):
        try:
            account_number = input("Enter your account number : ")
            pin = int(input("Enter your pin : "))

            userData = [i for i in self.data if i['account_number'] == account_number and i['pin'] == pin]

            if not userData:
                print("Invalid account number or pin")
                return

            choice = input("Press y if you want to delete your account or press n : ")
            if(choice.lower() == 'n'):
                return
            else:
                index = self.data.index(userData[0])                
                self.data.pop(index)
                print("Account Deleted Successfully")
                self.__update()
        except Exception as err:
            print(f"An error occurred: {err}")

    #check balance
    def checkBalance(self):
        try:
            account_number = input("Enter your account number : ")
            pin = int(input("Enter your pin : "))

            userData = [i for i in self.data if i['account_number'] == account_number and i['pin'] == pin]

            if not userData:
                print("Invalid account number or pin")
                return
            
            print("="*50)
            print(f"💰 Current Balance: ₹{userData[0]['balance']}")
            print("="*50)
        except Exception as err:
            print(f"An error occurred: {err}")

    #update database
    def __update(self):
        with open(Bank.DbPath,'w') as fs:
            fs.write(json.dumps(self.data , indent=4))

    #account number generate (static method)
    @staticmethod
    def __accountNumberGenerate():
        alpha = random.choices(string.ascii_letters , k=2)
        num = random.choices(string.digits , k=2)
        spChar = random.choices("@#$%&!^" , k=1)
        accNO = alpha+num+spChar
        random.shuffle(accNO)
        return ''.join(accNO)

#main function
def main():

    #object
    user = Bank()

    #menu
    print("\n" + "="*50)
    print("🏦 BANK ACCOUNT MANAGEMENT SYSTEM")
    print("="*50)
    print("Press 1 for creating an account")
    print("Press 2 for depositing the money in the bank account")
    print("Press 3 for withdrawing the money from the bank account")
    print("Press 4 for details")
    print("Press 5 for updating the account details")
    print("Press 6 for deleting the account")
    print("Press 7 for checking the balance of the bank account")
    print("Press 8 for exit the program")
    print("="*50)

    #input
    try:
        choice = int(input("Enter your choice : "))
        
        #choice
        if choice == 1:
            user.createAccount()
        elif choice == 2:
            user.deposit()
        elif choice == 3:
            user.withdraw()
        elif choice == 4:
            user.details()
        elif choice == 5:
            user.update()
        elif choice == 6:
            user.delete()
        elif choice == 7:
            user.checkBalance()
        elif choice == 8:
            print("Thank you for using our banking system! 👋")
            return
        else:
            print("❌ Invalid choice! Please enter a number between 1-8.")
            
    except ValueError:
        print("❌ Please enter a valid number!")
    except KeyboardInterrupt:
        print("\n\nThank you for using our banking system! 👋")
        return

if __name__ == "__main__":
    main()