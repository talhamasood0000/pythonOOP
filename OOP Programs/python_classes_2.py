# OOP by freecodecamp.org
class Item:
    pay_rate=0.8 #Payrate after 20% discout
    all=[]
    def __init__(self, name:str,price:int,quantity=0):

        #Run Validations
        assert price>=0, f"Price {price} is not greater than 0!"
        assert quantity>=0, f"Quantity {quantity} is not greater than 0!"

        #Assign to self object
        self.name=name
        self.price=price
        self.quantity=quantity

        #Append in the list
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price*self.quantity


    def apply_disount(self):
        self.price=self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"


# item1=Item("Phone",100,5)
# item1.apply_disount()
# print(item1.price)

# item2=Item("Laptop",1000,3)
# item2.pay_rate=0.5
# item2.apply_disount()
# print(item2.price)


#print(Item.pay_rate) #Accessing Class attributes
#print(item1.pay_rate) #it will search from instances and if not available then it will search in class level

#print(Item.__dict__) #class level
#print(item1.__dict__) #instance level


item1=Item("Phone",100,5)
item2=Item("Laptop",1000,3)
item3=Item("Charger",3000,6)
item4=Item("Tab",2000,4)
item2=Item("Cable",5000,7)

print(Item.all) #Append in the list "all"

# -> __repr__ (stands for representing your objects) it is almost similar to __str__*?

# for instance in Item.all:
#     print(instance.name)




















