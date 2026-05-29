
from exceptions.banking_exceptions import(
    InsufficientBalanceError,
    InvalidAmountError,
    DailyLimitExceededError
)
class BankAccount:

    bank_account_id=1001 

    def __init__(self, name, balance):

        self.name = name
        self.balance = balance
        self.transaction_history = []
        self.account_id=BankAccount.bank_account_id
        BankAccount.bank_account_id+=1



    def deposit(self, amount):
        if amount <=0:
          raise InvalidAmountError
        
        self.balance += amount

        self.transaction_history.append(("Cr", amount))

        return f"{amount} deposited successfully"


    def withdraw(self, amount):
        if amount <=0:
            raise InvalidAmountError
        
        if  amount <=50000:
           if self.balance >= amount:
                self.balance -= amount
                self.transaction_history.append(("Dr", amount))
                return "Withdrawal successful"
           else:
                    raise InsufficientBalanceError
        else :
            raise DailyLimitExceededError


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



b1=BankAccount("Aditya Chaudhary",1000000)
b2=BankAccount("Aditi Chaudhary",500)
print(b1.account_id)
print(b2.account_id)
print(b1.balance)
try:
    print(b1.withdraw(500))
    print(b1.deposit(0))
    print(b1.withdraw(999))
except (InsufficientBalanceError ,InvalidAmountError, DailyLimitExceededError) as e:
    print(e)
print(b1.transfer_to_account(54,b2))
print(b1.transaction_summary())
print(f"{b2.name}'s balance updated is :{b2.balance}")