# Concept : Class & Object

# Create a BankAccount class with attributes Account_Number, Owner_Name and balance.
# Add methods to deposite, withdraw and check balance.

# Create a class BankAccount
class BankAccount:
    Bank_Name = "State Bank of India"
    def __init__(self, Account_Number, Owner_Name, Balance): # Instance attribute
        self.Account_Number = Account_Number
        self. Owner_Name = Owner_Name
        self.Balance = Balance

    def deposite(self):
        deposite_amount = int(input("Enter amount for deposite : "))
        if(deposite_amount < 1):
            raise ValueError("Deposit amount must be positive")
        else:
            return deposite_amount + self.Balance
    
    def withdraw(self):
        withdraw_amount = int(input("Enter amount for withdraw : "))
        if(withdraw_amount < 1):
            raise ValueError("Withdraw amount must be positive")
        else:
            return self.Balance - withdraw_amount
    
    def check_balance(self):
        return self.Balance

# Object creation
person1 = BankAccount(156748678576, "Pritam", 5000)
person2 = BankAccount(256758345694, "Anurag", 4000)

# Specify here the person
print(f"{person2.Owner_Name} , current balance in your {BankAccount.Bank_Name} account is {person2.withdraw()}")