class Item:
    pay_rate = 0.8 # the pay rate after 20% discount
    def  __init__(self, name: str, price: float,  quantity=0):
        # run validations to the received arguments 
        assert price>=0,  f"Price {price} is not greater than or equal to zero!"
        assert quantity>=0 , f" quantity {quantity} is not greater than or equal to zero!"

        
       #assign to self object
        self.name= name
        self.name= price
        self.quantity= quantity 

    def calculate_total_price(self):
         return self.price * self.quantity
     
    def apply_discount(self ):
        self.price = self.price* pay_rate
item1 = Item(" Phone ", 2000, 5)
item2= Item(" laptop", 1000, 2)
 
print(Item.__dict__)
print(item1.__dict__)