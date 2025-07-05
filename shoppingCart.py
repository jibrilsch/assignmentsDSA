class shoppingCart:
    
    def __init__(self):
        self.items=[]
    
    def addItem(self,item_name:str,item_quantity:int,item_price:float):
        self.items.append((item_name,item_quantity,item_price))

    def removeItem(self,item_name:str):
        for item in self.items:
            if item[0]==item_name:
                self.items.remove(item)
                break

    def calculateTotal(self):
        total:float=0
        for name,quantity,price in self.items:
            total+=quantity*price
        return  total

    def cartContents(self):
        print("Cart contents:")
        for itemName,quantity,price in self.items:
            print(f"{itemName}- {quantity} @{price:.2f} each")
        print(f"Total:{self.calculateTotal():.2f}\n")


class discountedCart(shoppingCart):
    def __init__(self,discountRate:float):
        super().__init__()
        self.discountRate=discountRate


    def calculateTotal(self):
        return super().calculateTotal()*(1-self.discountRate)


class taxedCart(shoppingCart):
    def __init__(self,taxRate:float):
        super().__init__()
        self.taxRate=taxRate

    def calculateTotal(self):
        tax=super().calculateTotal()*self.taxRate
        return super().calculateTotal()+tax

def checkout(cart:shoppingCart):
    cart.cartContents()
    print(f"Total amount: {cart.calculateTotal():.3f}\n")

if __name__=="__main__":
    cartObject1=shoppingCart()
    print("Ordinary Shopping Cart without discounts or tax")
    cartObject1.addItem("Chocolate",2,185)
    cartObject1.addItem("Oreos",5,70)
    cartObject1.removeItem("Chocolate")
    cartObject1.cartContents()
    checkout(cartObject1)

    print("Shopping cart with a discount")
    cartObject2=discountedCart(0.25)
    cartObject2.addItem("Chocolate",5,200)
    checkout(cartObject2)

    print("Shopping cart with tax")
    cartObject3=taxedCart(0.14)
    cartObject3.addItem("Oreos",5,70)
    checkout(cartObject3)