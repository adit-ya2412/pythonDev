class Product:
    product_id_counter=1001


    def __str__(self):
        return(f"Product: {self.name} | Price: {self.price}| Quantity: {self.quantity}")
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
        self.product_id=Product.product_id_counter
        Product.product_id_counter+=1
        self.sales_history=[]
    
    def add_stock(self,amount):
        self.sales_history.append(("Ad",amount))
        self.quantity+=amount
        return "Quantity added succefully to product"
    
    def sell_stock(self,quantity):
        if self.quantity >= quantity:
            self.quantity-=quantity
            self.sales_history.append(("So",quantity))
            if self.quantity<5:
                print("Low Stock Warning")
        else :
            return "Not Enough Quantity"
        
        
        return "Quantity Sold Successfully"
    
    def update_price(self,new_price):
        if new_price >=0:
            self.price=new_price
            self.sales_history.append(("Up",new_price))
        else :
            return "Price cannot be zero or negative"
        return "Price changed Successfully"
    def product_summary(self):
        return {
            "Name":self.name,
            "Price":self.price,
            "Quantity":self.quantity
        }
    
    def inventory_value(self):
        return self.price * self.quantity
    
    def transaction_records(self):
        for trans in self.sales_history:
            if trans[0]=="So":
                print (f"Sold {trans[1]}  quantities")
            elif trans[0] == "Up":
                print (f"Added {trans[1]} quantities")
            else :
                print (f"Price Updated to {trans[1]}")
    


p1=Product("Laptop",80000,10)
p2=Product("Washing Machine",24000,9)
print(p1)
print(p1.add_stock(20))
print(p2.sell_stock(8))
print(p1.sell_stock(31))
print(p2.update_price(19000))
p1.transaction_records()
p2.transaction_records()