# OOP by freecodecamp.org
#Class Method
import csv

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

    @classmethod #Decorator(a quick way to change the behaviour of the function)
    def instantiate_from_csv(cls): #This method is Class Method. Means it can be accessed only from the class level
        #In class method class is send as the first argument 'cls'
        with open('items.csv','r') as f:
            reader=csv.DictReader(f) #Go and read the content as a dictionary
            items=list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=float(item.get('quantity'))
            )
    @staticmethod
    def is_integer(num):
        #We will count the floats that are point zero like 5.0, 67.0
        #isinstance is a built in function
        if isinstance(num,float): #If number is a floating number
            # Count the floats that are point zero
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False
            
    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"

Item.instantiate_from_csv()
print(Item.all)

print(Item.is_integer(7.0))

# item1=Item("Phone",100,5)
# item2=Item("Laptop",1000,3)
# item3=Item("Charger",3000,6)
# item4=Item("Tab",2000,4)
# item2=Item("Cable",5000,7)

## When to you class method and when to use static method
'''
class Item:
    @staticmethod
    def is_integer():

    This should do something that has a relationship with the class, 
    but not something that must be unique per instance!
'''
'''
    @classmethod
    def instantiate_from_csv(cls):
    
    This also should do something that has a relationship with the class,
    but ususlly, those are used to manipulate different structures of data 
    to instantiate objects, like we have done with csv
'''

# We usually donot call static and class method from the instance













