import csv

class Item:
    pay_rate=0.8 #Payrate after 20% discout
    all=[]
    def __init__(self, name:str,price:int,quantity=0):

        #Run Validations
        assert price>=0, f"Price {price} is not greater than 0!"
        assert quantity>=0, f"Quantity {quantity} is not greater than 0!"

        #Assign to self object
        self.__name=name    #_name
        self.price=price
        self.quantity=quantity

        #Append in the list
        Item.all.append(self)

    @property
    def name(self):
        return self.__name #_name

    @name.setter
    def name(self,value):
        self.__name=value

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

    # @property #Read Oly Attribute
    # def read_only_name(self):
    #     return "AAA"
    # -> We are no more allowed to change it



    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"
        #Generic way to represent the name of the class

