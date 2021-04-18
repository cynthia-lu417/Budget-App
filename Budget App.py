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
        selected_option = int(input("Select an option: \n"))

        while True:
            if (selected_option == 1):
                self.balance()

            elif (selected_option == 2):
                self.withdrawal()

            elif (selected_option == 3):
                self.deposit()

            else:
                print('Invalid option selected. Please, select a valid option')
                self.selected_option()
                continue  

    def get_balance(self):
        print(f"{self.category} have N-{self.balance}")
        return self.balance
        
    def deposit(self):
        amount = int(input("Enter an Amount to Deposit: \n"))

        self.balance += amount
        return "Deposit Successful"

    def withdrawal(self):
        amount = int(input("Enter an Amount to Withdraw: \n"))

        if self.balance >= amount:
                
            if amount >= 1000:
                self.balance -= amount
                print('You withdrew:', amount)

            else:
                print("Inavlid Amount Entered, please try again")
                self.withdrawal()
                    

        else:
            print("Insufficient Balance")
            self.user_option()

    def logout(self):
        selected_answer = int(input('Would you like to logout? 1) Yes 2) No \n'))
        if (selected_answer == 1):
            exit()

        else:
            user_option(self)

food = Budget("Food")
health = Budget("Health")
entertainment = Budget("Entertainment")

print("Welcome to Lulu's Budget app")
print("Category List")
print("1. Food")
print("2. Health")
print("3. Entertainment")
print("4. Logout")

cate= int(input("Select a category: \n"))
while True:
    if cate == 1:
        print(f"\n({food.category})")
        food.user_option()
        break

    elif cate == 2:
        print(f"\n({health.category})")
        health.user_option()
        break

    elif cate == 3:
        print(f"\n({entertainment.category})")
        entertainment.user_option()
        break

    else:
        print("Invalid option selected")
        cate = int(input("Select a category: \n"))
        continue
       
__init__()