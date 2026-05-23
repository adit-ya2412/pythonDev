from abc import ABC,abstractmethod

class PaymentMethod(ABC):
    
    def __init__(self,payment_method):
        self.payment_method=payment_method
        self.payment_history=[]
    @abstractmethod
    def process_payment(self,amount):
       pass
    @abstractmethod
    def refund_payment(self,amount):
       pass

    def log_transactions(self,amount):
        self.payment_history.append(f"{amount} paid ")



class UpiPayement(PaymentMethod):
    def __init__(self,upi_id,upi_pin):
        super().__init__("UPI")
        self.upi_id=upi_id
        self.upi_pin=upi_pin
    # def approve_payment(self,upi_pin):
    #     if self.upi_pin== upi_pin:
    #         return True
    #     else :
    #         return False
    def process_payment(self, amount):
        self.log_transactions(amount)
        return f"{amount} is paid  ,the upi id is {self.upi_id} "
        
    def refund_payment(self, amount):
        return f"{amount} reverted to upi_id {self.upi_id}"

class CreditCardPayment(PaymentMethod):

    def __init__(self, card_number,pin):
        super().__init__("Credit Card")
        self.card_number=card_number
        self.pin=pin
    
    
    
    def process_payment(self, amount):
            self.log_transactions(amount)
            car_number_ending_digits=  self.card_number[-4:]
            return f" {amount} paid . card number ending with {car_number_ending_digits}"
    
    def refund_payment(self, amount):
        car_number_ending_digits=  self.card_number[-4:]
        return f"{amount}refunded ,credited back to card ending with {car_number_ending_digits}"

    # def approve_payment(self,pin):
    #     if self.pin==pin:
    #         return True
    #     else:
    #         return False
        


class WalletPayment(PaymentMethod):
     
     def __init__(self, wallet_company,wallet_id):
         super().__init__("Wallet Payment")
         self.wallet_company=wallet_company
         self.wallet_id=wallet_id

     def process_payment(self, amount):
         self.log_transactions(amount)
         
         return f"{amount} paid , the wallet provider is {self.wallet_company} and the id is {self.wallet_id}"
     def refund_payment(self, amount):
         return f"the {amount} is credited back to {self.wallet_company} with id {self.wallet_id}"


class CryptoPayment(PaymentMethod):
    def __init__(self,wallet_address,blockchain_name):
        super().__init__("crypto")
        self.address=wallet_address
        self.chain_name=blockchain_name

    def process_payment(self, amount):
        self.log_transactions(amount)
        return f"{amount} paid from wallet with wallet_id {self.address} on the {self.chain_name} network"
    def refund_payment(self, amount):
        return f"{amount} is refunded to wallet id -> {self.address} on the {self.chain_name} network"

class PaymentProcessor():
    def make_payment(self,payment_method,amount):
        return payment_method.process_payment(amount)
    



        

p1=PaymentProcessor()
p2=PaymentProcessor()



c1=CreditCardPayment("122213489",9012)
upi1=UpiPayement("aditya@891",901243)
w1=WalletPayment("Paypal","22@fj1suyu")
crypto=CryptoPayment("ghhashjjfkkshhhhhereivnvlasm223454ng8gvp11283nvpn 2 fv=2ddac2212","Solana")

print(p1.make_payment(crypto,781209222222222))
print(p1.make_payment(upi1,500))
print(p2.make_payment(c1,320))


print(w1.process_payment(19920))
print(w1.refund_payment(19920))
print(w1.payment_history)

print(c1.process_payment(1892))
print(upi1.process_payment(1922))
print(c1.payment_history)
print(upi1.payment_history)