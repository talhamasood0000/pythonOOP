# OOP by freecodecamp.org
#Getters and Setters

'''
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
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"
        #Generic way to represent the name of the class

class Phone(Item):
# -> super allows the full control of the parent class methods
    def __init__(self, name:str,price:int,quantity=0, broken_phones=0):
        #Call to super function to have access to all attributes/ methods
        super().__init__(name,price,quantity)


        assert broken_phones>=0, f"Quantity {broken_phones} is not greater than 0!"

        self.broken_phones=broken_phones

'''
from item import Item
from phone import Phone

# Item.instantiate_from_csv()
# print(Item.all)

item1=Item("My Team",750)

item1.name="Other Team"
print(item1.name)

# item1._name="Other Item" #Now i can overwrite
# print(item1.name)
# print(item1.read_only_name)
# item1.read_only_name='BBB' #This will give error and will not allow you to make changes in it



#Encapsulation -> we want to restrict our user so that he cannot change the instances values randomly.