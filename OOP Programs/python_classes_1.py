# OOP by freecodecamp.org
'''
item1='Phone'
item1_price=500
item1_quantity=5
item1_price_total=item1_price*item1_quantity

print(type(item1)) #str
print(type(item1_price)) #int
print(type(item1_quantity)) #int
print(type(item1_price_total)) #int
'''

## Creating a class
# --Creating an instance or object is same thing
# --Class is a kind of a new data type so when we print type of an instance it outputs the name of class
# --methods are the functions in the classes
# __init__ is called a constructor. It is a method with a unique name

class Item:
    def __init__(self, name:str,price:int,quantity=0):
        #print("I am created Like that") #This line will always run when an instance is created of a class
        #print(f"An instance Created:{name}")

        #Run validation to the received arguments
        assert price>=0, f"Price {price} is not greater than 0!"
        assert quantity>=0, f"Quantity {quantity} is not greater than 0!"

        #Assign to self object
        self.name=name
        self.price=price
        self.quantity=quantity
    def calculate_total_price(self):
        return self.price*self.quantity

# ->create instance
# ->assign attributes . convention
# -> self in the function means that if i am calling hello.calculate_total_price() then it will send hello as a parameter in it always

'''
item1=Item("Phone",100)
#item1.name="Phone"

#print(item1.calculate_total_price(item1.price,item1.quantity))
print(item1.name)
print(item1.price)
print(item1.quantity)

item2=Item("Laptop",20,3)
#item2.name="Laptop"

#print(item2.calculate_total_price(item2.price,item2.quantity))


print(item2.name)
print(item2.price)
print(item2.quantity)
'''



item2=Item("Laptop",1,3)
item2.has_numpad=0
print(item2.calculate_total_price())

# -^ All these were instance attributes

