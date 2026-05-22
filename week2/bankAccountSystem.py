
    

class BankAccount:

    bank_account_id=1001 

    def __init__(self, name, balance):

        self.name = name
        self.balance = balance
        self.transaction_history = []
        self.account_id=BankAccount.bank_account_id
        BankAccount.bank_account_id+=1



    def deposit(self, amount):

        self.balance += amount

        self.transaction_history.append(("Cr", amount))

        return f"{amount} deposited successfully"


    def withdraw(self, amount):

        if self.balance >= amount:

            self.balance -= amount

            self.transaction_history.append(("Dr", amount))

            return "Withdrawal successful"

        return "Insufficient balance"


    def transfer_to_account(self, amount, account):

        if self.balance >= amount:

            self.balance -= amount
            account.balance += amount

            self.transaction_history.append(("Dr", amount))
            account.transaction_history.append(("Cr", amount))

            return "Transfer successful"

        return "Insufficient balance"


    def display_balance(self):

        return f"{self.name} balance: {self.balance}"


    def transaction_summary(self):

        for transaction_type, amount in self.transaction_history:

            if transaction_type == "Cr":
                print(f"Deposited {amount}")

            else:
                print(f"Withdrawn {amount}")

b1=BankAccount("Aditya Chaudhary",1000)
b2=BankAccount("Aditi Chaudhary",500)
print(b1.account_id)
print(b2.account_id)
print(b1.balance)
print(b1.withdraw(199))
print(b1.deposit(290))
print(b1.withdraw(999))
print(b1.transfer_to_account(54,b2))
print(b1.transaction_summary())
print(f"{b2.name}'s balance updated is :{b2.balance}")