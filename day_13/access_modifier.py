class BankAccount:
    def __init__(self, 
                 account_holder_name,
                 account_holder_address,
                 account_number,
                 balance = 0
                 ):
        
        self.account_holder_name = account_holder_name
        self.account_holder_address = account_holder_address
        self.account_number = account_number
        self.__balance = balance

    def print_details(self):
        print(f"Account Holder Name: {self.account_holder_name}")
        print(f"Account Holder Address:{self.account_holder_address} ")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.__balance}")


    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance = self.__balance - amount
            print(f"Withdrawn successful. Your new balance is {self.__balance}")
        else:
            print("Insufficient Balance")


    def deposit(self, amount):
        self.__balance = self.__balance + amount
        print(f"Deposit Successful. Your new balance is {self.__balance}")


ranjit_bank_account = BankAccount(
    "Ranjit Shrestha",
    "Kathmandu",
    4323435435345,
    1000
)



print("Enter 1 to withdraw.")
print("Enter 2 to deposit.")
print("====================")


choice = int(input("Enter your choice:"))

if choice == 1:
    amount = int(input("Enter amount you want to withdraw:"))
    ranjit_bank_account.withdraw(amount)

elif choice == 2:
    amount = int(input("Enter amount to deposit:"))
    ranjit_bank_account.deposit(amount)

else:
    print("Invalid Input")
