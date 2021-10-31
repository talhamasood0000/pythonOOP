from item import Item


class Phone(Item):

    def __init__(self, name:str,price:int,quantity=0, broken_phones=0):
        #Call to super function to have access to all attributes/ methods
        super().__init__(name,price,quantity)


        assert broken_phones>=0, f"Quantity {broken_phones} is not greater than 0!"

        self.broken_phones=broken_phones