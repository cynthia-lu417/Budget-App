import time
class Budget:
    def __init__(self, category):
        self.category = category
        self.balance = 0
        self.expenditure = 0    

    def user_option(self):  

        print('1. Check Balance')
        print('2. Withdrawal')
        print('3. Deposit')
        print('4. Transfer')
        selected_option = int(input("Select an option: \n"))

        while True:
            if (selected_option == 1):
                self.acc_balance()

            elif (selected_option == 2):
                self.withdrawal()

            elif (selected_option == 3):
                self.deposit()

            elif (selected_option == 4):
                self.transfer()

            else:
                print('Invalid option selected. Please, select a valid option')
                self.user_option()
                continue  

    def acc_balance(self):
        print(f"Total balance is  N", {self.balance})
        print("")
        self.logout()
        
        
    def deposit(self):
        amount = int(input("Enter an Amount to Deposit: \n"))

        self.balance += amount
        print(f"N{amount} added to {self.category}") 
        print("Deposit Successful")
        print("")
        self.logout()
        
        

    def withdrawal(self):
        amount = int(input("Enter an Amount to Withdraw: \n"))

        if self.balance >= amount:
                
            if amount >= 1000:
                self.balance -= amount
                self.expenditure += amount
                print('You withdrew: N', amount)
                self.logout()

            else:
                print("Invalid Amount Entered, please try again")
                self.withdrawal()
                    

        else:
            print("Insufficient Balance")
            self.user_option()

    def logout(self):
        selected_answer = int(input('Would you like to logout? 1) Yes 2) No \n'))
        if (selected_answer == 1):
            exit()

        else:
            self.user_option()

   
food = Budget("Food")
health = Budget("Health")
entertainment = Budget("Entertainment")

print("Welcome to Lulu's Budget app")
print("Category List")
print("1. Food")
print("2. Health")
print("3. Entertainment")

category = int(input("Select a category: \n"))
while True:
    if category == 1:
        print(f"\n({food.category})")
        food.user_option()
        break

    elif category == 2:
        print(f"\n({health.category})")
        health.user_option()
        break

    elif category == 3:
        print(f"\n({entertainment.category})")
        entertainment.user_option()
        break

    else:
        print("Invalid option selected")
        category = int(input("Select a category: \n"))
        continue
__init__()